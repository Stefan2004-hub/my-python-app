# Define variables to avoid repetition
PYTEST = uv run pytest
UTILS_TEST = tests/test_utils.py

.PHONY: test test-q test-file test-last

# 1. Run all tests (Standard)
test:
	$(PYTEST)

# 2. Run all tests quietly (The one you asked for)
test-q:
	$(PYTEST) -q

# 3. Run a specific file (utils)
test-utils:
	$(PYTEST) $(UTILS_TEST)

# 4. Run a test by name (Usage: make test-name NAME=reverse_string)
test-name:
	$(PYTEST) -k $(NAME)

# 5. Stop on first failure (Fail-fast)
test-x:
	$(PYTEST) -x