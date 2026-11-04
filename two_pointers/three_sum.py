"""
Problem: 3Sum
Find all unique triplets in an array that sum to zero.
Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2], [-1,0,1]]

Approach: Sort, fix one element, then solve the remaining two-sum with
two pointers. Skip duplicate values at every level to keep triplets
unique without a set of tuples.

Time Complexity: O(n^2)
Space Complexity: O(1) extra (excluding output and the sort)
"""

from __future__ import annotations


def three_sum(nums: list[int]) -> list[list[int]]:
    """Return all unique triplets that sum to zero."""
    nums = sorted(nums)
    result: list[list[int]] = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total == 0:
                result.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif total < 0:
                lo += 1
            else:
                hi -= 1
    return result


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    print("three_sum: OK")
