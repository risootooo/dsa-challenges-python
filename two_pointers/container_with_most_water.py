"""
Problem: Container With Most Water
Given heights of vertical lines, find two lines that, with the x-axis,
hold the most water.
Example: [1,8,6,2,5,4,8,3,7] -> 49

Approach: Two pointers at the ends. Area is width x min(height). Always
move the shorter side inward - moving the taller side can never help,
because width shrinks and height is capped by the shorter line.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def max_area(height: list[int]) -> int:
    """Return the maximum amount of water a container can store."""
    lo, hi = 0, len(height) - 1
    best = 0
    while lo < hi:
        best = max(best, (hi - lo) * min(height[lo], height[hi]))
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    print("container_with_most_water: OK")
