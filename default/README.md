# Example100 Math Operations

## Overview
This project implements basic math operations (addition and subtraction) with production-ready test automation and CI/CD integration.

## Usage
- Source functions are in `src/math_operations.py`
- Run tests using pytest:

```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## Workflow
- CI workflow file: `.github/workflows/ci.yml`
- All test files are in the `tests` folder.
- Requirements in `default/requirements.txt`
- Metadata for workflow generation in `default/math.json`

## Branches
- Default branch: `main`
- Feature branch: `Feature1`

## Test Reports
- Reports generated in `reports/` folder (junit and html formats).

## Requirements
- Python 3.10
- pytest==8.0.0
- pytest-html==4.1.1
