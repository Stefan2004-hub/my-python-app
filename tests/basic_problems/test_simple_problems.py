import pytest
from basic_problems import simple_problems


def test_two_sum_happy_path():
    # Arrange
    nums = [2, 7, 11, 15]
    target = 9

    # Act
    result = simple_problems.two_sum(nums, target)

    # Assert
    assert result == [0, 1]


def test_two_sum_invalid_input():
    with pytest.raises(ValueError, match="at least two elements"):
        simple_problems.two_sum(None, 9)

    with pytest.raises(ValueError, match="at least two elements"):
        simple_problems.two_sum([1], 9)


def test_two_sum_no_solution():
    with pytest.raises(ValueError, match="No two sum solution found"):
        simple_problems.two_sum([1, 2, 3], 10)


def test_is_palindrome_positive_match():
    assert simple_problems.is_palindrome(121) is True


def test_is_palindrome_negative_number():
    # Your specific Java test case
    assert simple_problems.is_palindrome(-121) is False


def test_is_palindrome_single_digit():
    assert simple_problems.is_palindrome(5) is True


def test_is_palindrome_mismatch():
    assert simple_problems.is_palindrome(10) is False
