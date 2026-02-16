# Example100 Math Operations

This repository provides basic math operations (addition, subtraction) as Python functions, along with comprehensive pytest test cases and CI workflow metadata for easy integration.

## Project Structure

- `src/` - Source code for math operations
- `tests/` - Pytest-based test cases
- `default/requirements.txt` - Python dependencies
- `default/math.json` - CI workflow metadata (for workflow generation)

## Usage

Install requirements:

```bash
pip install -r default/requirements.txt
```

Run tests:

```bash
pytest tests/
```

## Workflow Integration

- The `default/math.json` file contains all metadata required for CI pipeline generation.
- The recommended workflow file path is `.github/workflows/ci.yml`.

## Requirements

- Python 3.10+
- pytest
- pytest-html
