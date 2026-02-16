# Example100 Math Operations

## Overview
This repository implements basic math operations (addition and subtraction) in Python, with production-ready pytest test cases and CI/CD workflow integration.

## Folder Structure
- `src/`: Contains production code.
- `tests/`: Contains test files.
- `default/`: Contains requirements, metadata, and documentation.

## Usage
Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow
The workflow file is located at `.github/workflows/ci.yml`.

## Math Operations Example

```
from src.math_operations import add, subtract
print(add(2, 3))        # Returns 5
print(subtract(5, 3))   # Returns 2
```
