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
            print(f"  [MISSING] {pkg}")
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
    matrix_data = rng.normal(loc=0.0, scale=1.0, size=n_points)

    df = pd.DataFrame({
        'matrix_signal': matrix_data,
    })

    print("Generating visualization...")

    plt.hist(df['matrix_signal'], bins=30, edgecolor='black')
    plt.title('Matrix Data Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    output_file: str = 'matrix_analysis.png'
    plt.savefig(output_file)
    plt.close()

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    if not check_dependencies():
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
