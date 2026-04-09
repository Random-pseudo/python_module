import sys
import typing  # generic types for filelike objects


def read_file(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    file: typing.IO = open(filename, 'r')
    print("---")
    content: str = file.read()
    print(content)
    print("---")
    file.close()
    print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename: str = sys.argv[1]
    try:
        read_file(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
