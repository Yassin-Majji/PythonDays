from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.batches_processed = 0
        self.items_processed = 0
        self.last_status = "Ready"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if not isinstance(data_batch, list):
            return []

        if criteria is None:
            return [item for item in data_batch]

        return [
            item for item in data_batch
            if isinstance(item, str) and criteria.lower() in item.lower()
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "batches_processed": self.batches_processed,
            "items_processed": self.items_processed,
            "last_status": self.last_status,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")
        self.avg_temp = 0.0
        self.critical_alerts = 0

    def _parse_reading(
        self,
        item: Any
    ) -> Optional[Dict[str, Union[str, float]]]:
        if not isinstance(item, str) or ":" not in item:
            return None

        parts = item.split(":")
        if len(parts) != 2:
            return None

        reading_name = parts[0].strip().lower()

        try:
            reading_value = float(parts[1].strip())
        except ValueError:
            return None

        return {
            "name": reading_name,
            "value": reading_value,
        }

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if not isinstance(data_batch, list):
            return []

        valid_readings = [
            item for item in data_batch
            if self._parse_reading(item) is not None
        ]

        if criteria is None:
            return valid_readings

        if criteria.lower() == "critical":
            critical_items: List[Any] = []

            for item in valid_readings:
                reading = self._parse_reading(item)
                if reading is None:
                    continue

                name = reading["name"]
                value = reading["value"]

                if name == "temp" and value >= 30:
                    critical_items.append(item)
                elif name == "humidity" and value >= 80:
                    critical_items.append(item)
                elif (
                    name == "pressure"
                    and (value <= 980 or value >= 1030)
                ):
                    critical_items.append(item)

            return critical_items

        return super().filter_data(valid_readings, criteria)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise TypeError("Sensor batch must be a list.")

            parsed_readings = [
                self._parse_reading(item) for item in data_batch
            ]
            valid_readings = [
                reading for reading in parsed_readings
                if reading is not None
            ]

            if len(valid_readings) == 0:
                raise ValueError("No valid sensor readings found.")

            temp_values = [
                reading["value"]
                for reading in valid_readings
                if reading["name"] == "temp"
            ]

            if len(temp_values) > 0:
                self.avg_temp = sum(temp_values) / len(temp_values)

            critical_data = self.filter_data(data_batch, "critical")
            critical_count = len(critical_data)
            self.critical_alerts += critical_count

            self.batches_processed += 1
            self.items_processed += len(valid_readings)
            self.last_status = "Processed successfully"

            message = (
                f"Sensor analysis: "
                f"{len(valid_readings)} readings processed"
            )

            if len(temp_values) > 0:
                message += f", avg temp: {self.avg_temp:.1f}°C"

            if critical_count > 0:
                message += f", ALERT: {critical_count} extreme value"
                if critical_count > 1:
                    message += "s"
                message += " detected"

            return message

        except (TypeError, ValueError) as error:
            self.last_status = f"Failed: {error}"
            return f"Sensor stream error: {error}"
        except Exception as error:
            self.last_status = f"Failed: {error}"
            return f"Sensor stream unexpected error: {error}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["avg_temp"] = self.avg_temp
        stats["critical_alerts"] = self.critical_alerts
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        self.net_flow = 0.0
        self.large_transactions = 0

    def _parse_transaction(
        self,
        item: Any
    ) -> Optional[Dict[str, Union[str, float]]]:
        if not isinstance(item, str) or ":" not in item:
            return None

        parts = item.split(":")
        if len(parts) != 2:
            return None

        operation = parts[0].strip().lower()

        if operation not in ["buy", "sell"]:
            return None

        try:
            amount = float(parts[1].strip())
        except ValueError:
            return None

        return {
            "operation": operation,
            "amount": amount,
        }

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if not isinstance(data_batch, list):
            return []

        valid_transactions = [
            item for item in data_batch
            if self._parse_transaction(item) is not None
        ]

        if criteria is None:
            return valid_transactions

        if criteria.lower() == "large":
            large_items: List[Any] = []

            for item in valid_transactions:
                transaction = self._parse_transaction(item)
                if transaction is None:
                    continue

                if transaction["amount"] >= 100:
                    large_items.append(item)

            return large_items

        return super().filter_data(valid_transactions, criteria)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise TypeError("Transaction batch must be a list.")

            parsed_transactions = [
                self._parse_transaction(item) for item in data_batch
            ]
            valid_transactions = [
                transaction for transaction in parsed_transactions
                if transaction is not None
            ]

            if len(valid_transactions) == 0:
                raise ValueError("No valid transactions found.")

            buy_total = sum(
                transaction["amount"]
                for transaction in valid_transactions
                if transaction["operation"] == "buy"
            )
            sell_total = sum(
                transaction["amount"]
                for transaction in valid_transactions
                if transaction["operation"] == "sell"
            )

            batch_net_flow = buy_total - sell_total
            self.net_flow += batch_net_flow

            large_data = self.filter_data(data_batch, "large")
            self.large_transactions += len(large_data)

            self.batches_processed += 1
            self.items_processed += len(valid_transactions)
            self.last_status = "Processed successfully"

            return (
                f"Transaction analysis: "
                f"{len(valid_transactions)} operations, "
                f"net flow: {batch_net_flow:+.0f} units"
            )

        except (TypeError, ValueError) as error:
            self.last_status = f"Failed: {error}"
            return f"Transaction stream error: {error}"
        except Exception as error:
            self.last_status = f"Failed: {error}"
            return f"Transaction stream unexpected error: {error}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["net_flow"] = self.net_flow
        stats["large_transactions"] = self.large_transactions
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")
        self.error_count = 0
        self.critical_events = 0

    def _is_valid_event(self, item: Any) -> bool:
        return isinstance(item, str) and len(item.strip()) > 0

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if not isinstance(data_batch, list):
            return []

        valid_events = [
            item for item in data_batch
            if self._is_valid_event(item)
        ]

        if criteria is None:
            return valid_events

        if criteria.lower() == "critical":
            return [
                item for item in valid_events
                if item.lower() in [
                    "error",
                    "critical",
                    "alert",
                    "failure",
                ]
            ]

        return super().filter_data(valid_events, criteria)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise TypeError("Event batch must be a list.")

            valid_events = [
                item for item in data_batch
                if self._is_valid_event(item)
            ]

            if len(valid_events) == 0:
                raise ValueError("No valid events found.")

            errors_in_batch = [
                event for event in valid_events
                if event.lower() == "error"
            ]

            critical_in_batch = self.filter_data(valid_events, "critical")

            self.error_count += len(errors_in_batch)
            self.critical_events += len(critical_in_batch)

            self.batches_processed += 1
            self.items_processed += len(valid_events)
            self.last_status = "Processed successfully"

            return (
                f"Event analysis: {len(valid_events)} events, "
                f"{len(errors_in_batch)} error detected"
                f"{'' if len(errors_in_batch) == 1 else 's'}"
            )

        except (TypeError, ValueError) as error:
            self.last_status = f"Failed: {error}"
            return f"Event stream error: {error}"
        except Exception as error:
            self.last_status = f"Failed: {error}"
            return f"Event stream unexpected error: {error}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["error_count"] = self.error_count
        stats["critical_events"] = self.critical_events
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_stream(
        self,
        stream: DataStream,
        data_batch: List[Any]
    ) -> str:
        try:
            return stream.process_batch(data_batch)
        except Exception as error:
            return f"Processing failure in {stream.stream_id}: {error}"

    def process_all_streams(self, batches: List[List[Any]]) -> List[str]:
        results: List[str] = []

        for index, stream in enumerate(self.streams):
            if index < len(batches):
                batch = batches[index]
            else:
                batch = []

            results.append(self.process_stream(stream, batch))

        return results

    def get_all_stats(self) -> List[Dict[str, Union[str, int, float]]]:
        return [stream.get_stats() for stream in self.streams]


def format_batch(data_batch: List[Any]) -> str:
    return "[" + ", ".join(str(item) for item in data_batch) + "]"


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(
        f"Stream ID: {sensor_stream.stream_id}, "
        f"Type: {sensor_stream.stream_type}"
    )
    print(f"Processing sensor batch: {format_batch(sensor_batch)}")
    print(sensor_stream.process_batch(sensor_batch))
    print()

    print("Initializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANS_001")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(
        f"Stream ID: {transaction_stream.stream_id}, "
        f"Type: {transaction_stream.stream_type}"
    )
    print(
        f"Processing transaction batch: "
        f"{format_batch(transaction_batch)}"
    )
    print(transaction_stream.process_batch(transaction_batch))
    print()

    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    event_batch = ["login", "error", "logout"]
    print(
        f"Stream ID: {event_stream.stream_id}, "
        f"Type: {event_stream.stream_type}"
    )
    print(f"Processing event batch: {format_batch(event_batch)}")
    print(event_stream.process_batch(event_batch))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    mixed_batches = [
        ["temp:31", "humidity:85"],
        ["buy:120", "sell:30", "buy:80", "sell:25"],
        ["login", "error", "logout"],
    ]

    results = processor.process_all_streams(mixed_batches)

    print("Batch Results:")
    print(f"- Sensor data: {results[0]}")
    print(f"- Transaction data: {results[1]}")
    print(f"- Event data: {results[2]}")
    print()

    print("Stream filtering active: High-priority data only")
    filtered_sensor = sensor_stream.filter_data(mixed_batches[0], "critical")
    filtered_transactions = transaction_stream.filter_data(
        mixed_batches[1],
        "large"
    )
    print(
        f"Filtered results: {len(filtered_sensor)} "
        f"critical sensor alerts, "
        f"{len(filtered_transactions)} large transactions"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
