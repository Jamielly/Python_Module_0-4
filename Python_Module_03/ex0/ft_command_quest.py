#!/usr/bin/env python3
import sys


def command_quest() -> None:
    print("=== Command Quest ===")

    total_args: int = len(sys.argv)
    program_name: str = sys.argv[0]
    print(f"Program name: {program_name}")

    user_args: list[str] = sys.argv[1:]
    if not user_args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(user_args)}")
        for index, arg in enumerate(user_args, start=1):
            print(f"Argument {index}: {arg}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    command_quest()
