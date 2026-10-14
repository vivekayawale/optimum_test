# Python Practice Exercises

This project contains multiple Python exercises focused on problem-solving, logic building, and practical coding skills.

## Included Files

- `frequency_count_function.py` — counts the frequency of items in a list
- `list_comprehension_even_squares.py` — returns squares of positive even numbers using a list comprehension
- `corporate_id_validator.py` — validates a custom corporate ID format
- `.github/workflows/test.yml` — GitHub Actions workflow for running tests on Python 3.10, 3.11, and 3.12

## Exercise 1: Frequency Counter

Write a function that counts how many times each item appears in a list and returns the result as a dictionary.

### Example

```python
fruits = [
    "Apple", "Banana", "Mango", "apple",
    "Orange", "banana", "Grapes", "Mango",
    "APPLE", "Orange", "Pineapple", "Grapes"
]
```

Expected behavior: treat values case-insensitively, so `Apple`, `apple`, and `APPLE` are considered the same item.

### Run

```bash
python frequency_count_function.py
```

## Exercise 2: List Comprehension

Write a single-line Python function that returns the squares of only the positive even numbers in a list.

### Example

```python
numbers = [1, 2, 3, 4, 5, 6, -2, 8, 0]
```

Expected output:

```python
[4, 16, 36, 64]
```

### Run

```bash
python list_comprehension_even_squares.py
```

## Exercise 3: Corporate ID Validation

Write a function that validates a custom system ID string.

Requirements:
- must be a string
- must start with `CORP-`
- must be exactly 10 characters long
- must end with numeric digits

### Example

```python
"CORP-12345"  # valid
"CORP-abcde"  # invalid
"CORP-1234"   # invalid
```

### Run

```bash
python corporate_id_validator.py
```

## Exercise 4: GitHub Actions CI Workflow

The workflow in `.github/workflows/test.yml` runs automatically on push and pull request to the `main` branch.

It:
- uses Ubuntu as the runner
- tests across Python 3.10, 3.11, and 3.12
- caches pip dependencies
- installs dependencies from `requirements.txt`
- runs the test suite with `pytest`

## Practice Tips

- Keep logic simple and readable.
- Understand boundary conditions carefully.
- Test edge cases such as empty strings, wrong prefixes, negative values, and non-string inputs.
- Focus on time complexity and code clarity.

## Learning Goals

- Python basics
- Data structures and filtering
- String validation
- GitHub Actions automation
- Writing clean, reusable functions
