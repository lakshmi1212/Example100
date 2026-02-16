# Example100 Math Operations

This repository provides basic math operations (addition and subtraction) and comprehensive pytest-based test coverage, ready for CI/CD integration.

## Structure

- `src/`: Source code for math operations
- `tests/`: Pytest files for addition and subtraction
- `default/requirements.txt`: Project dependencies
- `default/math.json`: Workflow and meta information for automation

## Usage

### 1. Install dependencies

```bash
pip install -r default/requirements.txt
```

### 2. Run tests

```bash
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD Integration

- Workflow file: `.github/workflows/ci.yml`
- Uses Python 3.10, pytest, and pytest-html

## Meta Data

See `default/math.json` for workflow and automation metadata.
