class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass

def raise_custom_errors(step: str) -> None:
    if (step == "PlantError"):
        raise PlantError("The tomato plant is wilting!")
    elif (step == "WaterError"):
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    try:
        print("=== Custom Garden Errors Demo ===\n")
        custom_errors = ["PlantError", "WaterError", "GardenError"]
        for err in custom_errors:
            if (err == "PlantError" or err == "WaterError"):
                try:
                    print(f"Testing {err}...")
                    raise_custom_errors(err)
                except PlantError as e:
                    print(f"Caught {err}: {e}")
                except WaterError as e:
                    print(f"Caught {err}: {e}")
            elif err == "GardenError":
                print("Testing catching all garden errors...")
                errors = ["PlantError", "WaterError"]
                for er in errors:
                    try:
                        raise_custom_errors(er)
                    except GardenError as e:
                        print(f"Caught a garden error: {e}")
            print()
        print("All custom error types work correctly!")
    except Exception as e:
        print(f"Error: {e.args[0]}")


if __name__ == "__main__":
    test_custom_errors()