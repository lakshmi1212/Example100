# Example100 Math Operations

This repository implements basic math operations (addition and subtraction) in Python, with production-ready pytest test cases and CI/CD workflow integration.

## Folder Structure

- `src/` - Source code for math operations
- `tests/` - Pytest-based unit tests
- `default/` - Metadata, requirements, and documentation

## Usage

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```bash
   python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
   ```

## CI/CD Workflow
- The workflow file is located at `.github/workflows/ci.yml`.
- Tests run automatically on pushes to `Feature1` and pull requests to `main`.
- Reports are generated in the `reports/` directory.

## Math Operations

```
from src.math_operations import add, subtract

result1 = add(2, 3)         # 5
result2 = subtract(5, 2)    # 3
```
