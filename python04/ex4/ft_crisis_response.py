def open_files(file):
    with open(file, 'r') as f:
        content = f.read()
        print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed")


def main():
    files = ['lost_archive.txt', 'classified_vault.txt',
             'standard_archive.txt']

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    for f in files:
        try:
            open_files(f)
        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{f}'...")
            print('RESPONSE: Archive not found in storage matrix')
            print('STATUS: Crisis handled, system stable')
        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{f}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except Exception as e:
            print(f"Error: {e}")
        print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
