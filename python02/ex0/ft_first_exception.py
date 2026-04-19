def check_temperature(temp_str: str) -> int:
    print(f"Testing temperature: {temp_str}")
    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")

    if temperature > 40:
        raise ValueError(f"Error: {temperature}°C"
                         " is too hot for plants (max 40°C)")
    elif temperature < 0:
        raise ValueError(f"Error: {temperature}"
                         "°C is too cold for plants (min 0°C)")
    return temperature


def test_temperature_input() -> None:
    try:
        print("=== Garden Temperature Checker ===\n")
        tempr_list = ["25", "abc", "100", "-50"]

        for i in tempr_list:
            try:
                temp = check_temperature(i)
                print(f"Temperature {temp}°C is perfect for plants!")
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)
            print()
        print("All tests completed - program didn't crash!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_temperature_input()
