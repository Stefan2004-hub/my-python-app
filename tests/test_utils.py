from operator import concat

import pytest

from utils import utils


@pytest.mark.reverse_string
def test_reverse_string_basic():
    # Instead of assertEquals(expected, actual), we use 'assert'
    assert utils.reverse_string("fedora") == "arodef"


def test_reverse_string_empty():
    assert utils.reverse_string("") == ""


def test_reverse_string_with_spaces():
    assert utils.reverse_string("hi there") == "ereht ih"


@pytest.mark.count_word_occurrences
def test_count_word_occurrences_should_count_matches():
    # Arrange
    words = ["apple", "banana", "apple", "orange"]
    target = "apple"

    # Act
    result = utils.count_word_occurrences(words, target)

    # Assert (equivalent to assertEquals(2, result))
    assert result == 2


def test_count_word_occurrences_no_matches():
    assert utils.count_word_occurrences(["a", "b"], "c") == 0


@pytest.mark.remove_duplicates  # If you want to group these
def test_remove_duplicates_should_handle_duplicates_and_preserve_order():
    # Arrange
    input_list = ["apple", "banana", "apple", "orange"]
    expected = ["apple", "banana", "orange"]

    # Act
    result = utils.remove_duplicates(input_list)

    # Assert
    assert result == expected


def test_remove_duplicates_empty_list():
    assert utils.remove_duplicates([]) == []


def test_remove_duplicates_no_duplicates():
    input_list = ["a", "b", "c"]
    assert utils.remove_duplicates(input_list) == ["a", "b", "c"]


def test_concat_should_concatenate_strings():
    # Arrange & Act
    result = utils.concat(["Hello, ", "World!"])

    # Assert
    assert result == "Hello, World!"


def test_concat_with_none_input():
    # In Java, this was 'null'
    assert utils.concat(None) == ""


def test_concat_with_empty_list():
    assert utils.concat([]) == ""


def test_concat_skips_internal_nones():
    # Similar to your null check inside the loop
    assert utils.concat(["A", None, "B"]) == "AB"


def test_concat_procedural():
    # Standard case
    assert utils.concat_procedural(["Java", "To", "Python"]) == "JavaToPython"

    # Null element case
    assert utils.concat_procedural(["First", None, "Last"]) == "FirstLast"

    # Empty/None input cases
    assert utils.concat_procedural(None) == ""
    assert utils.concat_procedural([]) == ""
