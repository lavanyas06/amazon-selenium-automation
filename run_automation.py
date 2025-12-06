import sys
import subprocess
from pathlib import Path

TESTS = {
    "1": "tests/test_login.py",
    "2": "tests/test_search_product.py",
    "3": "tests/test_add_to_cart.py",
}

def run_test(option: str) -> int:
    test_path = TESTS.get(option)
    if not test_path:
        print("❌ Invalid option! Please choose 1, 2, or 3.")
        return 2
    path = Path(test_path)
    if not path.exists():
        print(f"❌ Test not found: {path}")
        return 3
    cmd = [sys.executable, "-m", "pytest", str(path)]
    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except Exception as e:
        print("❌ Failed to run test:", e)
        return 4

def main():
    print("🧠 Choose which automation to run:")
    print("1️⃣  Login Test")
    print("2️⃣  Search Product Test")
    print("3️⃣  Add to Cart Test")
    choice = input("Enter your choice (1/2/3): ").strip()
    rc = run_test(choice)
    if rc == 0:
        print("✅ Test run finished successfully.")
    else:
        print(f"🔚 Exit code: {rc}")

if __name__ == "__main__":
    main()