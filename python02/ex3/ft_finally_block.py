class WaterError(Exception):
    pass


def water_plants(plant_list: list) -> None:
    completed = 'y'
    print("Opening watering system")
    try:
        for plant in plant_list:
            is_empty = 'y'
            is_number = 'y'
            try:
                int(plant)
            except Exception:
                is_number = 'n'
            if (not plant) or (is_number == 'y'):
                if plant == "":
                    plant = "'empty-string'"
                raise WaterError(f"Error: Cannot water {plant} - invalid plant!")
            for i in plant:
                if (i != " "):
                    is_empty = 'n'
            if is_empty == 'y':
                raise WaterError("Error: Cannot water 'empty-string' - invalid plant!")
            else:
                print(f"Watering {plant}")

    except WaterError as e:
        print(e)
        completed = 'n'

    finally:
        print("Closing watering system (cleanup)")
        if (completed == 'y'):
            print("Watering completed successfully!")
        print()


def test_watering_system():
    print("=== Garden Watering System ===\n")
    try:
        print("Testing normal watering...")
        plants = ["tomato", "lettuce", "carrots"]
        water_plants(plants)
        print("Testing with error...")
        plants = ["tomato", None]
        water_plants(plants)
        print("Cleanup always happens, even with errors!")
    except Exception as e:
        print(f"Error: {e.args[0]}")


if __name__ == "__main__":
    test_watering_system()