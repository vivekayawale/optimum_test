from frequency_count_function import count_items
from list_comprehension_even_squares import square_even_positive
from corporate_id_validator import is_valid_corp_id


def test_count_items_case_insensitive():
    fruits = [
        "Apple", "Banana", "Mango", "apple",
        "Orange", "banana", "Grapes", "Mango",
        "APPLE", "Orange", "Pineapple", "Grapes"
    ]

    assert count_items(fruits) == {
        "apple": 3,
        "banana": 2,
        "mango": 2,
        "orange": 2,
        "grapes": 2,
        "pineapple": 1,
    }


def test_square_even_positive():
    numbers = [1, 2, 3, 4, 5, 6, -2, 8, 0]
    assert square_even_positive(numbers) == [4, 16, 36, 64]


def test_corporate_id_validator():
    assert is_valid_corp_id("CORP-12345") is True
    assert is_valid_corp_id("CORP-abcde") is False
    assert is_valid_corp_id("CORP-1234") is False
    assert is_valid_corp_id("ABC-12345") is False
    assert is_valid_corp_id(12345) is False
