#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    test_val = "25"
    print(f"\nInput data is '{test_val}'")
    try:
        temp = input_temperature(test_val)
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"\nCaught input_temperature error: {e}")

    test_inv = "abc"
    print(f"Input data is '{test_inv}'")
    try:
        temp = input_temperature(test_inv)
        print(f"\nTemperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
