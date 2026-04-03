from utils.utils import reverse_string


def test_reverse_string_basic():
    # Instead of assertEquals(expected, actual), we use 'assert'
    assert reverse_string("fedora") == "arodef"


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_reverse_string_with_spaces():
    assert reverse_string("hi there") == "ereht ih"
