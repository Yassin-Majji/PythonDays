import sys
import importlib
from importlib import util
from types import ModuleType
from typing import Optional


def check_package(name: str, description: str) -> Optional[ModuleType]:
    spec = util.find_spec(name)

    if spec is None:
        return None
    else:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - {description}")
        return module


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    pandas = check_package("pandas", "Data manipulation ready")
    numpy = check_package("numpy", "Numerical computation ready")
    requests = check_package("requests", "Network access ready")
    matplotlib = check_package("matplotlib", "Visualization ready")

    if not all([pandas, numpy, matplotlib, requests]):
        print("\nMissing dependencies. Please install "
              "them with one of this methods:")
        print("---> Using pip with requirements.txt:")
        print("          => pip install -r requirements.txt")

        print("---> Using Poetry with pyproject.toml:")
        print("          => poetry install")
        sys.exit(1)

    assert pandas is not None
    assert numpy is not None
    assert matplotlib is not None

    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")

    data = numpy.random.rand(1000)
    print("Processing 1000 data points...")

    data_frame = pandas.DataFrame(data, columns=["values"])

    print("Generating visualization...")
    plt.plot(data_frame["values"])
    plt.title("Matrix Data Analysis")
    plt.xlabel("Index")
    plt.ylabel("Value")

    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[Error] {e}")
