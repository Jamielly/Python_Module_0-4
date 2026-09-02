#!/usr/bin/env python3
import sys


def parse_arguments(args: list[str]) -> tuple[dict[str, int], list[str]]:
    inventory: dict[str, int] = {}
    insertion_order: list[str] = []

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(":", 1)
        item_name = parts.strip()
        quantity_str = parts[3].strip()

        if not item_name:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
            if quantity < 0:
                print(f"Quantity error for '{item_name}': negative quantity not allowed")
                continue
            inventory.update({item_name: quantity})
            insertion_order.append(item_name)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")

    return inventory, insertion_order


def analyze_inventory(inventory: dict[str, int], insertion_order: list[str]) -> None:
    if not inventory:
        print("Inventory is empty.")
        return

    print(f"Got inventory: {inventory}")

    items_list = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(items_list)} items: {total_qty}")

    for item in items_list:
        qty = inventory[item]
        percentage = (qty / total_qty) * 100 if total_qty > 0 else 0.0
        print(f"Item {item} represents {round(percentage, 1)}%")

    most_abundant = insertion_order
    least_abundant = insertion_order

    for item in insertion_order[1:]:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    raw_args = sys.argv[1:]
    if not raw_args:
        print("Got inventory: {}")
        return

    inventory, insertion_order = parse_arguments(raw_args)
    if inventory:
        analyze_inventory(inventory, insertion_order)


if __name__ == "__main__":
    main()
