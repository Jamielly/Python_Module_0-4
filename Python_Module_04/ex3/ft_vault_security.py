#!/usr/bin/env python3

def secure_archive(
    filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(filename, "r") as file_obj:
                data = file_obj.read()
            return True, data
        except OSError as e:
            return False, str(e)

    elif action == "write":
        try:
            with open(filename, "w") as file_obj:
                file_obj.write(content)
            return True, "Content successfully written to file"
        except OSError as e:
            return False, str(e)

    else:
        return False, f"Invalid action: '{action}'"


def main() -> None:
    print("=== Cyber Archives Security ===")

    res1 = secure_archive("/not/existing/file", "read")
    print(f"Using 'secure_archive' to read from a nonexistent file: {res1}")

    res2 = secure_archive("/etc/master.passwd", "read")
    print(f"Using 'secure_archive' to read from an inaccessible file: {res2}")

    res3 = secure_archive("ancient_fragment.txt", "read")
    print(f"Using 'secure_archive' to read from a regular file: {res3}")

    if res3:
        res4 = secure_archive("secure_out.txt", "write", res3[5])
        print(
            "Using 'secure_archive' to write previous content to a new file: "
            f"{res4}"
        )


if __name__ == "__main__":
    main()
