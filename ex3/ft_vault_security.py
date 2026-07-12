#!/usr/bin/python3


def secure_archive(
    filename: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:

    if action not in ("read", "write"):
        return (False, f"Invalid action '{action}'")
    mode: str = "r" if action == "read" else "w"
    try:
        with open(filename, mode) as file:
            if action == "read":
                return (True, file.read())
            file.write(content)
            return (True, content)
    except OSError as e:
        return (False, f"{e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    ok, data = secure_archive("vault.txt", "write", "top secret\n")
    print(ok, data)

    ok, data = secure_archive("vault.txt", "read")
    print(ok, data)

    ok, data = secure_archive("nope.txt", "read")
    print(ok, data)

    ok, data = secure_archive("vault.txt", "delete")
    print(ok, data)
