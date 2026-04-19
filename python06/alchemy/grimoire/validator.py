def validate_ingredients(ingredients: str) -> str:
    data = ["fire", "water", "earth", "air"]
    for v in data:
        if v in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} INVALID"
