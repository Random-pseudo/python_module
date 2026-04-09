def validate_ingredients(
    ingredients: str, allowed: list[str]
) -> str:
    ingredients_lower: str = ingredients.lower()
    for item in allowed:
        if item in ingredients_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
