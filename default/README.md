# Example100 Math Operations

This repository provides basic math operations (addition, subtraction) and corresponding unit tests.

## Structure

- `src/`: Production code for math operations
- `tests/`: Pytest-based unit tests for each operation
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI/CD workflow metadata (for workflow generation)

## Usage

```
from src.math_operations import add, subtract
print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

## Testing

Run all tests with:
```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD

See `.github/workflows/ci.yml` for the workflow (generated via math.json).
