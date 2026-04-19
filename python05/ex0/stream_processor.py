from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataProcessor(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result

    def validation_success_message(self) -> str:
        return "data verified"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def _is_valid_number(self, value: Any) -> bool:
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def _build_numeric_result(self, data: List[Union[int, float]]) -> str:
        total = sum(data)
        average = total / len(data)
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={total}, avg={average}"
        )

    def validate(self, data: Any) -> bool:
        if self._is_valid_number(data):
            return True

        if isinstance(data, list) and len(data) > 0:
            return all(self._is_valid_number(item) for item in data)

        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError(
                    "NumericProcessor requires a number or a "
                    "non-empty list of numbers."
                )

            if self._is_valid_number(data):
                numeric_data = [data]
            else:
                numeric_data = data

            return self.format_output(
                self._build_numeric_result(numeric_data)
            )
        except ValueError as e:
            raise ValueError(f"Numeric processing error: {e}")

    def format_output(self, result: str) -> str:
        return super().format_output(f"[NUMERIC] {result}")

    def validation_success_message(self) -> str:
        parent_message_success = super().validation_success_message()
        return f"Numeric {parent_message_success}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def _count_words(self, data: str) -> int:
        return len(data.split())

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data.strip()) > 0

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError(
                    "TextProcessor requires a non-empty string."
                )
            result = (
                f"Processed text: {len(data)} characters, "
                f"{self._count_words(data)} words"
            )
            return self.format_output(result)
        except ValueError as e:
            raise ValueError(f"Text processing error: {e}")

    def format_output(self, result: str) -> str:
        return super().format_output(f"[TEXT] {result}")

    def validation_success_message(self) -> str:
        parent_message_success = super().validation_success_message()
        return f"Text {parent_message_success}"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def _extract_log_parts(self, data: str) -> Optional[Dict[str, str]]:
        if not isinstance(data, str) or ":" not in data:
            return None

        parts = data.split(":", 1)
        level = parts[0].strip().upper()
        message = parts[1].strip()

        if level not in ["INFO", "WARNING", "ERROR", "DEBUG"]:
            return None
        if message == "":
            return None

        return {"level": level, "message": message}

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return self._extract_log_parts(data) is not None

    def process(self, data: Any) -> str:
        try:
            parts = self._extract_log_parts(data)
            if parts is None:
                raise ValueError(
                    "LogProcessor requires text in the format "
                    "LEVEL: message."
                )

            result = (
                f"{parts['level']} level detected: "
                f"{parts['message']}"
            )
            return self.format_output(result)
        except ValueError as e:
            raise ValueError(f"Log processing error: {e}")

    def format_output(self, result: str) -> str:
        level = result.split(" ", 1)[0]

        if level == "ERROR":
            prefix = "[ALERT]"
        elif level == "WARNING":
            prefix = "[WARNING]"
        else:
            prefix = f"[{level}]"

        return super().format_output(f"{prefix} {result}")

    def validation_success_message(self) -> str:
        return "Log entry verified"


def display_data(data: Any) -> str:
    if isinstance(data, str):
        return f'"{data}"'
    return str(data)


def run_single_demo(processor: DataProcessor, data: Any) -> None:
    print(f"Initializing {processor.name}...")
    print(f"Processing data: {display_data(data)}")

    try:
        if not processor.validate(data):
            raise ValueError("Validation failed")

        print(f"Validation: {processor.validation_success_message()}")
        print(f"Output: {processor.process(data)}")
    except ValueError as e:
        print(f"Error: {e}")
    print()


def run_polymorphic_demo(
    processors: List[DataProcessor],
    data_items: List[Any]
) -> None:
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    for index, processor in enumerate(processors):
        try:
            result = processor.process(data_items[index])
            print(f"Result {index + 1}: {result}")
        except ValueError as e:
            print(f"Result {index + 1}: Error - {e}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    run_single_demo(numeric_processor, [1, 2, 3, 4, 5])
    run_single_demo(numeric_processor, 7)
    run_single_demo(text_processor, "Hello Nexus World")
    run_single_demo(log_processor, "ERROR: Connection timeout")

    polymorphic_processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    polymorphic_data = [
        [1, 2, 3],
        "Hello Matrix",
        "INFO: System ready",
    ]

    run_polymorphic_demo(polymorphic_processors, polymorphic_data)
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
