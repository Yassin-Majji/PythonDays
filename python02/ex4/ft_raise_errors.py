def check_plant_health(plant_name: str, water_level: int, sunlight_hoursi: int) -> str:
    is_empty = True
    for i in plant_name:
        if (i != ' '):
            is_empty = False
    if (is_empty):
        print("Testing empty plant name...")
        raise ValueError("Error: Plant name cannot be empty!")
    if (water_level > 10):
        print("Testing bad water level...")
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    elif (water_level < 1):
        print("Testing bad water level...")
        raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
    
    if (sunlight_hoursi > 12):
        print("Testing bad sunlight hours...")
        raise ValueError(f"Error: Sunlight hours {sunlight_hoursi} is too high (max 12)")
    elif (sunlight_hoursi < 2):
        print("Testing bad sunlight hours...")
        raise ValueError(f"Error: Sunlight hours {sunlight_hoursi} is too low (min 2)")
    print("Testing good values...")
    return (f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    try:
        print("=== Garden Plant Health Checker ===\n")
        plants_data = [("tomato", 5, 6), ("", 5, 6), ("tomato", 15, 6), ("tomato", 5, 0)]
        for name, level, sunlight in plants_data:
            try:
                massage_return = check_plant_health(name, level, sunlight)
                print(massage_return)
            except ValueError as e:
                print(e)
            print()
        print("All error raising tests completed!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_plant_checks()
