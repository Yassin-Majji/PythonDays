import sys
import os
import site


def is_in_global_env() -> bool:
    return sys.prefix == sys.base_prefix


def global_env() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")

    print("\nThen run this program again")


def venv() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")

    print("\nPackage installation path:")
    print(site.getsitepackages()[0])


def main() -> None:
    if is_in_global_env():
        global_env()
    else:
        venv()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
