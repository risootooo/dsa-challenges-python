"""
Problem: Two Sum
Given an array and a target, return the indices of the two numbers that
add up to the target. Exactly one solution is assumed.
Example: nums=[2, 7, 11, 15], target=9 -> [0, 1]

Approach: One pass with a hash map from value to index. For each number,
check whether its complement (target - value) was already seen.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of the two elements that sum to ``target``."""
    seen: dict[int, int] = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], i]
        seen[value] = i
    raise ValueError("no two elements sum to target")


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("two_sum: OK")
