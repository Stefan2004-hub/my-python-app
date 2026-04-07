from typing import List


def count_derogatory_comments(keyword: str, comments: List[str]) -> int:
    """
    Counts comments containing a keyword as a case-insensitive substring.
    Time Complexity: O(n * m) | Space Complexity: O(1)
    """
    if not keyword or comments is None:
        return 0

    count = 0
    # Normalize the keyword once outside the loop
    normalized_keyword = keyword.lower()

    for comment in comments:
        # Python's 'in' operator is the equivalent of Java's '.contains()'
        if normalized_keyword in comment.lower():
            count += 1

    return count


def count_derogatory_comments_fast(keyword: str, comments: List[str]) -> int:
    k = keyword.lower()
    return sum(1 for c in comments if k in c.lower())
