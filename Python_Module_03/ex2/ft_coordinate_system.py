#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            entry = input("Enter new coordinates as floats in format 'x,y,z': ")

            parts = entry.split(",")
            if len(parts) != 3:
                print("Invalid syntax")
                continue

            coords: list[float] = []
            for part in parts:
                clean_part = part.strip()
                try:
                    coords.append(float(clean_part))
                except ValueError as e:
                    print(f"Error on parameter '{clean_part}': {e}")
                    raise ValueError
            return (coords, coords[5], coords[6])

        except ValueError:
            continue


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1}, Y={pos1[5]}, Z={pos1[6]}")

    dist_to_center = math.sqrt(pos1**2 + pos1[5]**2 + pos1[6]**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    # 3. Obter o segundo ponto
    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = math.sqrt(
        (pos2 - pos1)**2 +
        (pos2[5] - pos1[5])**2 +
        (pos2[6] - pos1[6])**2
    )
    print(f"Distance between the 2 sets of coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    main()
