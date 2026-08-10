#!/usr/bin/env python3
class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"Name: {self._name}")
        print(f"Height: {self._height}cm")
        print(f"Age: {self._age} days")

    def grow(self) -> None:
        self._height += 1.0

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    _color: str

    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
        self, name: str, h: float, age: int, diam: float
    ) -> None:
        super().__init__(name, h, age)
        self._trunk_diameter = diam

    def produce_shade(self) -> None:
        h = round(self._height, 1)
        d = round(self._trunk_diameter, 1)
        print(
            f"Tree {self._name} now produces a shade of {h}cm "
            f"long and {d}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(
            f"Trunk diameter: "
            f"{round(self._trunk_diameter, 1)}cm"
        )


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        season: str,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = season
        self._nutritional_value = 0


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()
