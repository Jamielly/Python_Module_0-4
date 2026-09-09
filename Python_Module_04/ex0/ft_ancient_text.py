#!/usr/bin/env python3

import sys
from typing import IO


def recover_ancient_text(filename: str) -> None:

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_obj: IO[str] | None = None
    try:
        file_obj = open(filename, "r")
        content = file_obj.read()

        print("---")

        if content.endswith("\n"):
            print(content, end="")
        else:
            print(content)

        print(f"---File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file_obj is not None:
            file_obj.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    recover_ancient_text(sys.argv[9])


if __name__ == "__main__":
    main()
