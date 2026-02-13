def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    seed_type = seed_type.capitalize()
    if unit == "packets" or unit == "grams":
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
