# my-python-app

`my-python-app` is a small educational Python project that demonstrates a clean project layout, simple utility functions, and basic automated testing with `pytest`.

The repository currently includes a minimal application entrypoint plus a set of string and list helpers implemented in `src/utils/utils.py`. It is intended as a practical learning project rather than a production package.

## Features

- String reversal helpers, including a manual implementation and a slicing-based variant
- Word occurrence counting for lists of strings
- Duplicate removal while preserving insertion order
- String concatenation helpers that handle `None` values safely
- Automated tests with `pytest`

## Requirements

- Python `3.14` or newer
- [`uv`](https://docs.astral.sh/uv/) for environment and dependency management

## Setup

Clone the repository and install the project dependencies:

```bash
uv sync
```

## Run the App

Run the current application entrypoint with:

```bash
uv run python main.py
```

Current behavior:

- Prints a greeting
- Prints example values for `var1` and `var2`
- Demonstrates the `reverse_string()` utility

Example output:

```text
Hello from my-python-app!
var1: value1
var2: value2
the reversed string is: !dlroW ,olleH
```

## Run the Tests

Execute the test suite with:

```bash
uv run pytest -q
```

The current test suite covers the utility functions in `src/utils/utils.py`.

## Project Structure

```text
my-python-app/
├── main.py
├── pyproject.toml
├── src/
│   └── utils/
│       ├── __init__.py
│       └── utils.py
└── tests/
    └── test_utils.py
```

## Example Usage

You can import and use the utility functions directly:

```python
from utils.utils import (
    concat,
    count_word_occurrences,
    remove_duplicates,
    reverse_string,
)

print(reverse_string("fedora"))
# arodef

print(count_word_occurrences(["apple", "banana", "apple"], "apple"))
# 2

print(remove_duplicates(["apple", "banana", "apple", "orange"]))
# ['apple', 'banana', 'orange']

print(concat(["Hello, ", None, "World!"]))
# Hello, World!
```

## Notes

- This project is currently best viewed as a learning/demo repository.
- The package metadata and application description are still minimal and can be expanded as the project grows.
- If the project evolves further, useful next steps would include adding a CLI, richer package metadata, and CI automation.
