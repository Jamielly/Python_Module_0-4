#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(
            self,
            message: str = "A generic garden error occurred."
            ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(
            self,
            message: str = "Unknown plant error."
            ) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(
            self,
            message: str = "Unknown water error."
            ) -> None:
        super().__init__(message)


def check_plant(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water(tank_empty: bool) -> None:
    if tank_empty:
        raise WaterError("Not enough water in the tank!")


def check_garden() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant(True)
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("Testing WaterError...")
    try:
        check_water(True)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("Testing catching all garden errors...")
    try:
        check_plant(True)
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        check_water(True)
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    check_garden()
