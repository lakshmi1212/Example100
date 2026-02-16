# Example100 Math Operations

## Overview
This repository provides basic math operations (addition and subtraction) and corresponding automated tests using pytest.

## Structure
- `src/`: Source code for math operations
- `tests/`: Pytest test cases for the functions
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI/CD workflow metadata

## Usage

### Math Operations
```
from src.math_operations import add, subtract

result1 = add(5, 3)        # 8
result2 = subtract(5, 3)   # 2
```

### Running Tests
Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests:
```
pytest tests/
```

## CI/CD
This repository is configured for GitHub Actions CI via `.github/workflows/ci.yml` (see `default/math.json` for workflow metadata).
