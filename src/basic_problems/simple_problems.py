from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Returns the indices of two numbers that add up to the target.
    Time Complexity: O(n) | Space Complexity: O(n)
    """
    # 1. Validation
    if nums is None or len(nums) < 2:
        raise ValueError("Input array must have at least two elements")

    # 2. Map (Dictionary) to store: {value: index}
    num_to_index = {}

    # 3. enumerate() provides both the index (i) and the value (num)
    for i, num in enumerate(nums):
        complement = target - num

        # Checking 'if x in dict' is O(1) in Python
        if complement in num_to_index:
            return [num_to_index[complement], i]

        num_to_index[num] = i

    # 4. If we reach the end, no solution was found
    raise ValueError("No two sum solution found")
