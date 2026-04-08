import sys
import typing


def read_file(filename: str) -> str:
    print(f"Accessing file '{filename}'")
    file: typing.IO = open(filename, 'r')
    print("---")
    content: str = file.read()
    print(content, end='')
    print("---")
    file.close()
    print(f"File '{filename}' closed.")
    return content


def transform_content(content: str) -> str:
    lines: list = content.splitlines()
    new_lines: list = [line + '#' for line in lines]
    return '\n'.join(new_lines) + '\n'


def save_file(filename: str, content: str) -> None:
    print(f"Saving data to '{filename}'")
    file: typing.IO = open(filename, 'w')
    file.write(content)
    file.close()
    print(f"Data saved in file '{filename}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        content: str = read_file(filename)
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("\nTransform data:")
    new_content: str = transform_content(content)
    print("---")
    print(new_content, end='')
    print("---")

    dest: str = input("\nEnter new file name (or empty): ")
    if not dest:
        print("Not saving data.")
        return

    try:
        save_file(dest, new_content)
    except OSError as e:
        print(f"Error opening file '{dest}': {e}")


if __name__ == "__main__":
    main()
