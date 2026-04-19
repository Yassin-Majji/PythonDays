import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n", file=sys.stdout)

    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    print()
    print("[STANDARD] Archive status from "
          f"{archivist_id}: {status_report}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()
    print("Three-channel communication test successful.")


if __name__ == '__main__':
    try:
        main()
    except (Exception, KeyboardInterrupt) as e:
        print(f"Error: {e}")
