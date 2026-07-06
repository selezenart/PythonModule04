#!/usr/bin/python3
import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1], "r")
        print("---")
        print(file.read())
        print("---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
