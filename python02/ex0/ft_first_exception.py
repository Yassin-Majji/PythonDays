def check_temperature(temp_str: str) -> int:
    try:
        print(f"Testing temperature: {temp_str}")
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
        print("d")
    except Exception as e:
        print(e)


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    tempr_list = ["None", "abc", "100", "-50"]

    for i in tempr_list:
        try:
            temp = check_temperature(i)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as e:
            print(e)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
