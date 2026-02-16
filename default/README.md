# Example100 Math Operations

## Overview

This repository provides basic math operations (addition and subtraction) in Python, along with comprehensive pytest-based test coverage and CI workflow integration.

## Usage

Import and use the functions from `src/math_operations.py`:

```python
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

## Running Tests

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run all tests:

```bash
pytest tests/
```

## CI Workflow

The repository includes a GitHub Actions workflow at `.github/workflows/ci.yml` for automated testing and reporting.

## Structure

- `src/`: Source code
- `tests/`: Test cases
- `default/`: Documentation, requirements, and metadata

## Meta Data

See `default/math.json` for workflow metadata.
