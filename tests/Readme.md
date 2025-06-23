---

# Tests

This directory contains unit and functional tests for the **AirBnB Clone** project.

## Purpose

The tests are designed to ensure the correctness and stability of the core components, including:

* The command interpreter (`console.py`)
* Data models in the `models/` directory
* File and database storage engines
* The API (if implemented)

## How to Run Tests

To run all tests, use the following command:

```bash
python3 -m unittest discover tests
```

Or, to run a specific test file:

```bash
python3 -m unittest tests/test_models/test_user.py
```

## Directory Structure

```
tests/
├── test_console.py            # Tests for the command interpreter
├── test_models/
│   ├── test_base_model.py     # Tests for BaseModel
│   ├── test_user.py           # Tests for User model
│   └── ...                    # Other model tests
```

---
