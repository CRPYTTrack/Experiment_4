# Calculator Project

This is a simple Python calculator that includes unit tests using `pytest`.

## 🛠️ Setup and Installation

If you are setting this project up on a new PC, the most reliable way to install the required tools without running into environment issues is to use `python -m pip`.

1. **Upgrade pip (Recommended)**:
   ```bash
   python -m pip install --upgrade pip
   ```

2. **Install pytest**:
   ```bash
   python -m pip install pytest
   ```

## 🚀 Running the Tests

To run the unit tests perfectly across any computer, avoid using IDE "Run" buttons (which run tests as standard scripts without output) or plain `pytest` commands (which can cause PATH issues). 

Instead, run the tests module directly through Python in your terminal:

```bash
python -m pytest test_calculator.py
```

### Additional Testing Commands
* **Verbose output** (See the names of every test passing):
  ```bash
  python -m pytest -v test_calculator.py
  ```
* **Show print statements** (If you added `print()` inside your tests for debugging):
  ```bash
  python -m pytest -s test_calculator.py
  ```
