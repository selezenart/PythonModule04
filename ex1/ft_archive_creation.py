#!/usr/bin/python3
import sys
import typing


if __name__ == "__main__":
    buffer: list[str] = []
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        sys.exit(1)
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.IO[str] = open(sys.argv[1], "r")
        print("---")
        for line in file:
            print(line, end="")
            buffer.append(line)
        print("\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
        transformed: list[str] = []
        for line in buffer:
            transformed.append(line.rstrip("\n") + "#\n")
        print("Transform data:")
        print("---")
        for line in transformed:
            print(line, end="")
        print("---")
        new_file_name = input("Enter new file name (or empty): ")
        if not new_file_name:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file_name}'")
            new_file: typing.IO[str] = open(new_file_name, "w")
            for line in transformed:
                new_file.write(line)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
