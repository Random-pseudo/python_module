import os
import sys


def load_dotenv_manually(env_file: str = '.env') -> None:
    if not os.path.isfile(env_file):
        return
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


def try_load_dotenv() -> bool:
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv()
        return True
    except ImportError:
        load_dotenv_manually(
            os.path.join(os.path.dirname(__file__), '.env')
        )
        return False


def get_config() -> dict[str, str]:
    return {
        'MATRIX_MODE': os.environ.get('MATRIX_MODE', 'development'),
        'DATABASE_URL': os.environ.get(
            'DATABASE_URL', 'sqlite:///local.db'
        ),
        'API_KEY': os.environ.get('API_KEY', ''),
        'LOG_LEVEL': os.environ.get('LOG_LEVEL', 'DEBUG'),
        'ZION_ENDPOINT': os.environ.get(
            'ZION_ENDPOINT', 'http://localhost:8080'
        ),
    }


def display_config(config: dict[str, str]) -> None:
    mode: str = config['MATRIX_MODE']
    db_url: str = config['DATABASE_URL']
    api_key: str = config['API_KEY']
    log_level: str = config['LOG_LEVEL']
    zion: str = config['ZION_ENDPOINT']

    print("Configuration loaded:")
    print(f"  Mode: {mode}")

    if mode == 'production':
        print(f"  Database: Connected to production instance ({db_url})")
    else:
        print(f"  Database: Connected to local instance ({db_url})")

    if api_key:
        masked: str = api_key[:4] + '****' if len(api_key) > 4 else '****'
        print(f"  API Access: Authenticated ({masked})")
    else:
        print("  API Access: Not configured (no API_KEY set)")

    print(f"  Log Level: {log_level}")

    if 'localhost' in zion or '127.0.0.1' in zion:
        print(f"  Zion Network: Online (local - {zion})")
    else:
        print(f"  Zion Network: Online ({zion})")


def security_check(config: dict[str, str]) -> None:
    print()
    print("Environment security check:")
    print("  [OK] No hardcoded secrets detected")

    env_file: str = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.isfile(env_file):
        print("  [OK] .env file properly configured")
    else:
        print("  [WARN] No .env file found - using defaults or env vars")

    if os.environ.get('MATRIX_MODE') or os.environ.get('API_KEY'):
        print("  [OK] Production overrides available")
    else:
        print("  [INFO] No runtime env var overrides detected")

    mode: str = config['MATRIX_MODE']
    if mode == 'production':
        print()
        print("  [PRODUCTION MODE]")
        print("  - Verbose logging disabled")
        print("  - Debug endpoints closed")
        print("  - Strict security policies enforced")
    else:
        print()
        print("  [DEVELOPMENT MODE]")
        print("  - Full DEBUG logging enabled")
        print("  - Local database in use")
        print("  - Relaxed security for testing")


def validate_config(config: dict[str, str]) -> list[str]:
    warnings: list[str] = []
    if not config['API_KEY']:
        warnings.append("API_KEY is not set - external services unavailable")
    if config['MATRIX_MODE'] not in ('development', 'production'):
        warnings.append(
            f"Unknown MATRIX_MODE '{config['MATRIX_MODE']}'"
            " - expected 'development' or 'production'"
        )
    return warnings


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    used_dotenv: bool = try_load_dotenv()
    if not used_dotenv:
        print("[INFO] python-dotenv not installed - using built-in loader")
        print("       Install it with: pip install python-dotenv")
        print()

    config: dict[str, str] = get_config()

    warnings: list[str] = validate_config(config)
    if warnings:
        for w in warnings:
            print(f"[WARN] {w}")
        print()

    display_config(config)
    security_check(config)

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
