#!/usr/bin/env python3

import sys
from typing import IO


def recover_and_preserve(filename: str) -> None:

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_obj: IO[str] | None = None
    content: str = ""

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
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        return
    finally:
        if file_obj is not None:
            file_obj.close()

    lines = content.splitlines()
    transformed_lines = [f"{line}#" for line in lines]
    transformed_content = "\n".join(transformed_lines) + "\n"

    print("Transform data:")
    print("---")
    print(transformed_content, end="")
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    try:
        new_filename = sys.stdin.readline()
        new_filename = new_filename.strip()
    except (EOFError, KeyboardInterrupt):
        new_filename = ""

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")

    out_file_obj: IO[str] | None = None
    try:
        out_file_obj = open(new_filename, "w")
        out_file_obj.write(transformed_content)
        print(f"Data saved in file '{new_filename}'.")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error saving file '{new_filename}': {e}\n")
        sys.stderr.flush()
    finally:
        if out_file_obj is not None:
            out_file_obj.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    recover_and_preserve(sys.argv[6])


if __name__ == "__main__":
    main()
