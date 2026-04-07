from utils import logic


def test_count_derogatory_comments_case_insensitive():
    # Arrange
    comments = ["bad_word_here", "this_is_Fine", "BAD_news", "no_bad_vibes"]
    keyword = "bad"

    # Act
    result = logic.count_derogatory_comments(keyword, comments)

    # Assert
    assert result == 3


def test_count_derogatory_comments_no_matches():
    assert logic.count_derogatory_comments("safe", ["hello", "world"]) == 0


def test_count_derogatory_comments_empty_input():
    assert logic.count_derogatory_comments("bad", []) == 0
    assert logic.count_derogatory_comments("", ["bad"]) == 0
