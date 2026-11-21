"""
Problem: Trapping Rain Water
Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after
raining.
Example: height=[0,1,0,2,1,0,1,3,2,1,2,1] -> 6; height=[4,2,0,3,2,5] -> 9

Approach: Two pointers from both ends. The water above a bar is
bounded by the lower of the tallest bar to its left and the tallest
bar to its right. Keeping the running maxima on each side, always
advance the side with the smaller maximum: that side's bound is
already decided by its own maximum (the other side is at least as
tall), so the water at that bar can be settled in one step without
precomputing prefix/suffix arrays. Negative heights are invalid
input and raise ValueError; an empty map traps nothing.

Time Complexity: O(n) — each pointer moves at most n steps
Space Complexity: O(1) extra
"""

from __future__ import annotations


def trap(height: list[int]) -> int:
    """Total units of rain water trapped by the elevation map."""
    if any(h < 0 for h in height):
        raise ValueError("heights must be non-negative")
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


if __name__ == "__main__":
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([3, 0, 3]) == 3
    assert trap([1, 2, 3, 4]) == 0
    assert trap([4, 3, 2, 1]) == 0
    # Edge cases: empty, single bar, flat map
    assert trap([]) == 0
    assert trap([5]) == 0
    assert trap([2, 2, 2]) == 0
    try:
        trap([1, -1, 2])
    except ValueError:
        pass
    else:
        raise AssertionError("negative height must raise ValueError")
    print("trapping_rain_water: OK")
