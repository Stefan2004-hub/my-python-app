from typing import List, Optional


def reverse_string(text: str) -> str:
    """
    Reverses a string using manual character traversal.
    Time: O(n) | Space: O(n)
    """
    reversed_chars = []
    # range(start, stop, step) -> similar to your for loop
    for i in range(len(text) - 1, -1, -1):
        reversed_chars.append(text[i])

    return "".join(reversed_chars)


# The "Pythonic" way (Slicing) - much faster in practice
def reverse_string_fast(text: str) -> str:
    return text[::-1]


def count_word_occurrences(words: List[str], word_to_count: str) -> int:
    """
    Counts occurrences of a target word in a list of words.
    Time Complexity: O(n) | Space Complexity: O(1)
    """
    # The "Java-like" way (Manual Traversal)
    count = 0
    for word in words:
        if word == word_to_count:  # Python '==' is like Java '.equals()'
            count += 1
    return count


def count_word_occurrences_pythonic(words: List[str], word_to_count: str) -> int:
    """The idiomatic way to do it in Python."""
    return words.count(word_to_count)


def remove_duplicates(items: List[str]) -> List[str]:
    """
    Removes duplicate items while preserving insertion order.
    Time Complexity: O(n) | Space Complexity: O(n)
    """
    # dict.fromkeys creates a concat_proceduraldictionary with items as keys (which are unique)
    # Since Python 3.7, dicts preserve insertion order.
    return list(dict.fromkeys(items))


def concat(strings: Optional[List[Optional[str]]]) -> str:
    """
    Concatenates a list of strings end-to-end.
    Time Complexity: O(n) | Space Complexity: O(n)
    """
    # 1. Defensive check (None is Python's null)
    if not strings:
        return ""

    # 2. Filter out None elements and join
    # This is a 'generator expression' - it's like a Java Stream
    return "".join(s for s in strings if s is not None)


def concat_procedural(strings):
    """
    Concatenates a list of strings end-to-end.
    Direct procedural implementation (StringBuilder style).
    """
    # 1. Defensive check for None (null) or empty list
    if strings is None or len(strings) == 0:
        return ""

    # 2. This list acts as our 'StringBuilder' buffer
    buffer = []

    for s in strings:
        # 3. Explicit null check
        if s is not None:
            buffer.append(s)

    # 4. Final conversion to string
    return "".join(buffer)


def find_smallest_interval(numbers: List[int]) -> int:
    """
    Finds the smallest positive interval between any two numbers.
    Time Complexity: O(n log n) | Space Complexity: O(n)
    """
    # 1. Validation (Equivalent to Java's IllegalArgumentException)
    if numbers is None:
        raise ValueError("numbers must not be None")

    if len(numbers) < 2:
        raise ValueError("numbers must contain at least 2 elements")

    # 2. Sort the list (O(n log n))
    # sorted() creates a new list, leaving the original untouched
    sorted_nums = sorted(numbers)

    # 3. Initialize with infinity
    min_interval = float("inf")

    # 4. Compare adjacent elements (O(n))
    for i in range(len(sorted_nums) - 1):
        current_interval = sorted_nums[i + 1] - sorted_nums[i]

        if current_interval < min_interval:
            min_interval = current_interval

        # Early exit optimization
        if min_interval == 0:
            return 0

    return int(min_interval)
