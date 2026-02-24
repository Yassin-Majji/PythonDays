def garden_operations(step: str):
    if step == "ValueError":
        try:
            print(f"Testing {step}...")
            int("abc")
        except ValueError:
            raise ValueError(f"Caught {step}: invalid literal for int()")
    elif step == "ZeroDivisionError":
        try:
            print(f"Testing {step}...")
            7 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError(f"Caught {step}: division by zero")
    elif step == "FileNotFoundError":
        try:
            print(f"Testing {step}...")
            file = "missing.txt"
            open(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Caught {step}: No such file '{file}'")
    elif step == "KeyError":
        try:
            print(f"Testing {step}...")
            d = {"name": "ahmed"}
            print(d["age"])
        except KeyError:
            raise KeyError(f"Caught {step}: 'missing\\_plant'")
    elif


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    list_errors = ["ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError", "MultipleError"]
    for i in list_errors:
        try:
            garden_operations(i)
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except KeyError as e:
            print(e)
        print("\n")
    print("Testing multiple errors together...")
    print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
