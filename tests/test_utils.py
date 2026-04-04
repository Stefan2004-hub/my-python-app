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
