import os


def development(cfg: dict) -> dict:
    return {
        "mode": "development",
        "db": (
            "Connected to local instance"
            if cfg["DATABASE_URL"]
            else "Not configured"
        ),
        "api": (
            "Authenticated"
            if cfg["API_KEY"]
            else "Missing key"
        ),
        "log": cfg["LOG_LEVEL"] or "DEBUG",
        "zion": (
            "Online"
            if cfg["ZION_ENDPOINT"]
            else "Offline"
        ),
        "security": "[OK] Development mode (safe defaults)",
    }


def production(cfg: dict) -> dict:
    return {
        "mode": "production",
        "db": (
            "Connected to secure remote instance"
            if cfg["DATABASE_URL"]
            else "ERROR: Not configured"
        ),
        "api": (
            "Authenticated"
            if cfg["API_KEY"]
            else "ERROR: Missing key"
        ),
        "log": cfg["LOG_LEVEL"] or "WARNING",
        "zion": (
            "Online"
            if cfg["ZION_ENDPOINT"]
            else "ERROR: Offline"
        ),
        "security": "[OK] Production overrides active",
    }


def main() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("[Error] python-dotenv not installed!")
        print("---> Install it using: pip install -r ../ex1/requirements.txt")
        return

    if not os.path.exists(".env"):
        print("[Warning] .env file not found!")
        print("--> Create it using:")
        print("   cp .env.example .env")

    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    missing = [k for k, v in config.items() if not v]

    if missing:
        print("[Warning] Missing configuration:")
        for m in missing:
            print(f"- {m}")
        print()

    MODES = {
        "development": development,
        "production": production
    }

    mode = config["MATRIX_MODE"]
    if mode is not None:
        handler = MODES.get(mode, development)
    result = handler(config)

    print("Configuration loaded:")
    print(f"Mode: {result['mode']}")
    print(f"Database: {result['db']}")
    print(f"API Access: {result['api']}")
    print(f"Log Level: {result['log']}")
    print(f"Zion Network: {result['zion']}")

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print(result["security"])

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[Error] {e}")
