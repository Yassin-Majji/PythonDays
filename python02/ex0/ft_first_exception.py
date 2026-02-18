def check_temperature(temp_str):
        try:
            print(f"Testing temperature: {temp_str}")
            temperature = int(temp_str)
        except ValueError:
            raise ValueError(f"Error: '{temp_str}' is not a valid number\n")
            return
        if (temperature >= 0 and temperature <= 40):
            print(f"Temperature {temperature}°C is perfect for plants!\n")
        elif temperature > 40:
            raise ValueError(f"Error: {temperature}°C is too hot for plants (max 40°C)\n")
        else:
            raise ValueError(f"Error: {temperature}°C is too cold for plants (min 0°C)\n")
        
def test_temperature_input():
        print("=== Garden Temperature Checker ===\n")
        try:
            check_temperature("25")
        except ValueError as e:
            print(e)
        try:
            check_temperature("abc")
        except ValueError as e:
            print(e)
        try:
            check_temperature("100")
        except ValueError as e:
            print(e)
        try:
            check_temperature("-50")
        except ValueError as e:
            print(e)
        finally:
             print("All tests completed - program didn't crash!")

test_temperature_input()