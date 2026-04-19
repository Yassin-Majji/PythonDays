import sys


def main() -> None:
    print("=== Command Quest ===")
    size = len(sys.argv)
    if (size < 2):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print("Program name: ", end="")
        if (size == 4):
            for char in sys.argv[0]:
                if (char == '_'):
                    print("\\", end="")
                print(char, end="")
            print()
        else:
            print(sys.argv[0])
        print(f"Arguments received: {size - 1}")
        i = 1
        while (i < size):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {size}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
