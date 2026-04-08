def secure_archive(
    filename: str,
    action: str = 'read',
    content: str = ''
) -> tuple:
    if action == 'read':
        try:
            with open(filename, 'r') as f:
                data: str = f.read()
            return (True, data)
        except OSError as e:
            return (False, str(e))
    elif action == 'write':
        try:
            with open(filename, 'w') as f:
                f.write(content)
            return (True, 'Content successfully written to file')
        except OSError as e:
            return (False, str(e))
    else:
        return (False, f"Unknown action: '{action}'")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd'))

    print("\nUsing 'secure_archive' to read from a regular file:")
    result: tuple = secure_archive('ancient_fragment.txt')
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive('new_vault_file.txt', 'write', result[1]))


if __name__ == "__main__":
    main()
