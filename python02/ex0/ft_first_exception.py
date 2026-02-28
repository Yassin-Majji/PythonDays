def check_temperature(temp_str: str) -> int:
    try:
        print(f"Testing temperature: {temp_str}")
        if (temp_str is None):
            raise Exception(f"Error: '{temp_str}' is not a valid number")
        temperature = int(temp_str)
        if (temperature >= 0 and temperature <= 40):
            return temperature
        elif temperature > 40:
            raise Exception(f"Error: {temperature}°C"
                            " is too hot for plants (max 40°C)")
        else:
            raise Exception(f"Error: {temperature}"
                            "°C is too cold for plants (min 0°C)")
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    x = range(3)
    tempr_list = ["25", "abc", "100", "-50", None, x]

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


if __name__ == "__main__":
    test_temperature_input()
