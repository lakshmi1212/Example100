# Example100 Math Operations

## Overview
This project provides basic math operations (addition, subtraction) with production-ready test automation and CI/CD integration.

## Usage

Import math_operations from src:

```
from src.math_operations import add, subtract
```

## Running Tests

Install dependencies from requirements.txt:

```
pip install -r default/requirements.txt
```

Run tests with pytest:

```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD Workflow

See `.github/workflows/ci.yml` for automated testing instructions.
