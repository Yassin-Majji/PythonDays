def main() -> None:
    file = open("new_discovery.txt", "w")
    data = "[ENTRY 001] New quantum algorithm discovered\n" \
           "[ENTRY 002] Efficiency increased by 347%\n" \
           "[ENTRY 003] Archived by Data Archivist trainee"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    file.write(data)
    print(data)

    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
