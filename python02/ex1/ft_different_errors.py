def garden_operations(step: str) -> None:
    if step == "ValueError":
        int("abc")

    elif step == "ZeroDivisionError":
        7 / 0
    elif step == "FileNotFoundError":
        f = open("missing.txt")
        f.close()

    elif step == "KeyError":
        d = {"name": "ahmed"}
        print(d["missing\\_plant"])

    elif step == "MultipleError":
        d = {"name": "ahmed"}
        print(d["missing\\_plant"])

        int("abc")

        f = open("missing.txt")
        f.close()


def test_error_types() -> None:
    try:
        print("=== Garden Error Types Demo ===\n")
        list_errors = ["ValueError", "ZeroDivisionError", "FileNotFoundError",
                       "KeyError", "MultipleError"]
        for err in list_errors:
            if (err != "MultipleError"):
                try:
                    print(f"Testing {err}...")
                    garden_operations(err)
                except ValueError:
                    print(f"Caught {err}: invalid literal for int()")
                except ZeroDivisionError:
                    print(f"Caught {err}: division by zero")
                except FileNotFoundError as e:
                    print(f"Caught {err}: "
                          f"No such file '{e.filename}'")
                except KeyError as e:
                    print(f"Caught {err}: '{e.args[0]}'")
                print()
            else:
                try:
                    print("Testing multiple errors together...")
                    garden_operations(err)
                except (ValueError, ZeroDivisionError, FileNotFoundError,
                        KeyError):
                    print("Caught an error, but program continues!")
        print("\nAll error types tested successfully!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_error_types()
