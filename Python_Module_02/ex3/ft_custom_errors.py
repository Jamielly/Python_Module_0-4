#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str = "A generic garden error occurred.") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error.") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error.") -> None:
        super().__init__(message)


def trigger_plant_issue(is_wilting: bool) -> None:
    Args:
        is_wilting (bool): 
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def trigger_water_issue(tank_empty: bool) -> None:
    Args:
        tank_empty (bool): 
    if tank_empty:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        trigger_plant_issue(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        trigger_water_issue(True)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        trigger_plant_issue(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        trigger_water_issue(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
