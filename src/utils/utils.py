from typing import List


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
        if word == word_to_count: # Python '==' is like Java '.equals()'
            count += 1
    return count

def count_word_occurrences_pythonic(words: List[str], word_to_count: str) -> int:
    """The idiomatic way to do it in Python."""
    return words.count(word_to_count)