
def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    f = None
    try:
        f = open("ancient_fragment.txt", 'r')
        print("Connection established...")
        content = f.read()
        print("\nRECOVERED DATA:")
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")
    except (FileNotFoundError, PermissionError):
        print("ERROR: Storage vault not found. Run data generator first.")

    finally:
        if f:
            f.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
