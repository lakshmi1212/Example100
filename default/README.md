# Example100 Math Operations

## Overview
This project provides basic math operations (addition and subtraction) with production-grade test automation and CI/CD integration.

## Usage

Python functions are available in `src/math_operations.py`:

```
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 1)
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run tests:

```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## Workflow

CI pipeline is configured in `.github/workflows/ci.yml`.
Pushes to `Feature1` and PRs to `main` trigger the workflow.

## Test Reports

Test reports are generated in the `reports/` directory in both JUnit and HTML formats.

## Requirements

- Python 3.10+
- pytest
- pytest-html

## Repository Structure

- src/: Source code
- tests/: Test files
- default/: Project meta files
