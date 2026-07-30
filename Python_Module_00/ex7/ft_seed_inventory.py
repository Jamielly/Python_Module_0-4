def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type_capit = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed_type_capit} seeds: {quantity} packets available")
    if (unit == "grams"):
        print(f"{seed_type_capit} seeds: {quantity} grams total")
    if (unit == "area"):
        print(f"{seed_type_capit} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
