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