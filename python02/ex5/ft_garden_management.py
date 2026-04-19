class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []
        self.water_tank = 100

    def __validate_plant_name(self, plant_name: str) -> None:
        if plant_name is None:
            raise PlantError("Plant name cannot be empty!")

        is_empty = 1

        try:
            for char in plant_name:
                if char != " ":
                    is_empty = 0
        except TypeError:
            raise PlantError("Plant name must be text!")

        if is_empty == 1:
            raise PlantError("Plant name cannot be empty!")

        try:
            int(plant_name)
            raise PlantError("Plant name cannot be only numbers!")
        except ValueError:
            pass

    def add_plant(self, plant_name):
        self.__validate_plant_name(plant_name)

        for plant in self.plants:
            if plant == plant_name:
                raise PlantError(f"Plant '{plant_name}' "
                                 "already exists in garden!")

        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        is_work = 0
        try:
            for plant in self.plants:
                if self.water_tank < 5:
                    raise WaterError("Not enough water in tank")
                if is_work == 0:
                    print("Opening watering system")
                print(f"Watering {plant} - success")
                self.water_tank = self.water_tank - 5
                is_work = 1
        finally:
            if (is_work == 1):
                print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> str:
        self.__validate_plant_name(plant_name)
        it_found = 0
        for plant in self.plants:
            if (plant == plant_name):
                it_found = 1
        if it_found == 0:
            raise ValueError(f"'{plant_name}' this plant it not exist!")

        if water_level < 1:
            raise ValueError(f"Water level {water_level}"
                             " is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Water level {water_level}"
                             " is too high (max 10)")

        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too high (max 12)")

        return (f"{plant_name}: healthy (water: {water_level},"
                f" sun: {sunlight_hours})")


def test_garden_management() -> None:
    try:
        manager = GardenManager()

        print("=== Garden Management System ===\n")

        print("Adding plants to garden...")
        plants_to_add = [7, "lettuce", ""]
        for plant in plants_to_add:
            try:
                manager.add_plant(plant)
            except PlantError as e:
                print(f"Error adding plant: {e}")
        print()

        print("Watering plants...")
        try:
            manager.water_plants()
        except WaterError as e:
            print(f"Caught WaterError: {e}")
        print()

        print("Checking plant health...")
        plant_checks = [
            ("tomato", 5, 8),
            ("lettuce", 15, 8)
        ]
        for name, water, sun in plant_checks:
            try:
                result = manager.check_plant_health(name, water, sun)
                print(result)
            except ValueError as e:
                print(f"Error checking plant: {e}")
            except Exception as e:
                print(e)
        print()

        print("Testing error recovery...")
        manager.water_tank = 4
        try:
            manager.water_plants()
        except GardenError as e:
            print(f"Caught GardenError: {e}")

        print("System recovered and continuing...")

        print("\nGarden management system test complete!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_garden_management()
