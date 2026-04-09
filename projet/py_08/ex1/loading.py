import sys
import importlib


REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}

OPTIONAL_PACKAGES: dict[str, str] = {
    "requests": "Network access ready",
}


def check_package(name: str) -> tuple[bool, str]:
    try:
        mod = importlib.import_module(name)
        version: str = getattr(mod, '__version__', 'unknown')
        return (True, version)
    except ImportError:
        return (False, '')


def check_dependencies() -> bool:
    print("Checking dependencies:")
    all_ok: bool = True

    for pkg, label in REQUIRED_PACKAGES.items():
        ok, version = check_package(pkg)
        if ok:
            print(f"  [OK] {pkg} ({version}) - {label}")
        else:
            print(f"  [MISSING] {pkg} - {label}")
            all_ok = False

    for pkg, label in OPTIONAL_PACKAGES.items():
        ok, version = check_package(pkg)
        if ok:
            print(f"  [OK] {pkg} ({version}) - {label}")

    if not all_ok:
        print()
        print("Missing dependencies! Install them with:")
        print()
        print("  Using pip:")
        print("    pip install -r requirements.txt")
        print()
        print("  Using Poetry:")
        print("    poetry install")

    return all_ok


def show_package_manager_info() -> None:
    print()
    print("--- Dependency Manager Comparison ---")
    print("pip:")
    print("  - Simple, built-in Python tool")
    print("  - Uses requirements.txt for dependency listing")
    print("  - No lock file by default (use pip freeze)")
    print("  - Install: pip install -r requirements.txt")
    print()
    print("Poetry:")
    print("  - Modern dependency manager with lock file")
    print("  - Uses pyproject.toml (PEP 517/518 standard)")
    print("  - Generates poetry.lock for reproducible builds")
    print("  - Install: poetry install")
    print("  - Run:     poetry run python loading.py")


def run_analysis() -> None:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib  # type: ignore
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt  # type: ignore

    print()
    print("Analyzing Matrix data...")

    n_points: int = 1000
    print(f"Processing {n_points} data points...")

    rng = np.random.default_rng(seed=42)
    timestamps = np.arange(n_points)
    signal = rng.normal(loc=0.0, scale=1.0, size=n_points)
    noise = rng.uniform(low=-0.5, high=0.5, size=n_points)
    matrix_data = signal + noise

    df = pd.DataFrame({
        'timestamp': timestamps,
        'matrix_signal': matrix_data,
        'rolling_mean': pd.Series(matrix_data).rolling(window=50).mean(),
    })

    print("Generating visualization...")

    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle('Matrix Data Analysis', fontsize=14, fontweight='bold')

    axes[0].plot(
        df['timestamp'], df['matrix_signal'],
        color='green', alpha=0.6, linewidth=0.8, label='Raw Signal'
    )
    axes[0].plot(
        df['timestamp'], df['rolling_mean'],
        color='lime', linewidth=2, label='Rolling Mean (50)'
    )
    axes[0].set_title('Matrix Signal Over Time')
    axes[0].set_xlabel('Timestamp')
    axes[0].set_ylabel('Signal Value')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_facecolor('#0a0a0a')
    axes[0].figure.set_facecolor('#1a1a1a')  # type: ignore

    axes[1].hist(
        df['matrix_signal'].dropna(),
        bins=50, color='green', alpha=0.7, edgecolor='lime'
    )
    axes[1].set_title('Signal Distribution')
    axes[1].set_xlabel('Value')
    axes[1].set_ylabel('Frequency')
    axes[1].grid(True, alpha=0.3)
    axes[1].set_facecolor('#0a0a0a')

    plt.tight_layout()
    output_file: str = 'matrix_analysis.png'
    plt.savefig(output_file, dpi=100, bbox_inches='tight')
    plt.close()

    mean_val: float = float(df['matrix_signal'].mean())
    std_val: float = float(df['matrix_signal'].std())
    print(f"  Mean signal: {mean_val:.4f}")
    print(f"  Std deviation: {std_val:.4f}")
    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    if not check_dependencies():
        show_package_manager_info()
        sys.exit(1)

    show_package_manager_info()
    run_analysis()


if __name__ == "__main__":
    main()
