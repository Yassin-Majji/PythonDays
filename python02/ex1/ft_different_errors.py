def garden_operations(step: str):
    if step == "ValueError":
            int("abc")

    elif step == "ZeroDivisionError":
            7 / 0
    elif step == "FileNotFoundError":
            open("missing.txt")

    elif step == "KeyError":
            d = {"name": "ahmed"}
            print(d["missing\\_plant"])

    elif step == "MultipleError":
         d = {"name": "ahmed"}
         print(d["missing\\_plant"])

         int("abc")

         open("missing.txt")



def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    list_errors = ["ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError", "MultipleError"]
    for err in list_errors:
        if(err != "MultipleError"):
            try:
                print(f"Testing {err}...")
                garden_operations(err)
            except ValueError:
                print(f"Caught {err}: invalid literal for int()")
            except ZeroDivisionError:
                print(f"Caught {err}: division by zero")
            except FileNotFoundError as e:
                print(f"Caught FileNotFoundError: No such file '{e.filename}'")
            except KeyError as e:
                print(f"Caught {err}: '{e.args[0]}'")
            print()
        else:
            try:
                  print("Testing multiple errors together...")
                  garden_operations(err)
            except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
                print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
