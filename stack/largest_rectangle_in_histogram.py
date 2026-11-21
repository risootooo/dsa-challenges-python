"""
Problem: Largest Rectangle in Histogram
Given an array of integers heights representing a histogram's bar
heights where the width of each bar is 1, return the area of the
largest rectangle in the histogram.
Example: heights=[2,1,5,6,2,3] -> 10 (bars 5 and 6, height 5);
heights=[2,4] -> 4

Approach: Monotonic increasing stack of bar indices. Scanning left
to right (plus a sentinel bar of height 0 at the end), whenever the
current bar is shorter than the bar on top of the stack, that stacked
bar's rectangle can be finalised: its height is the bar's height, its
right boundary is the current index, and its left boundary is the new
stack top (the previous shorter bar). Each index is pushed and popped
at most once, so the scan is linear. Negative heights are invalid
input and raise ValueError; an empty histogram has area 0.

Time Complexity: O(n) — each bar is pushed/popped at most once
Space Complexity: O(n) for the stack
"""

from __future__ import annotations


def largest_rectangle_area(heights: list[int]) -> int:
    """Area of the largest rectangle contained in the histogram."""
    if any(h < 0 for h in heights):
        raise ValueError("heights must be non-negative")
    best = 0
    stack: list[int] = []  # indices with non-decreasing heights
    for i in range(len(heights) + 1):
        current = heights[i] if i < len(heights) else 0  # sentinel
        while stack and current < heights[stack[-1]]:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, h * (i - left - 1))
        stack.append(i)
    return best


if __name__ == "__main__":
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([5, 5, 5]) == 15
    assert largest_rectangle_area([1, 2, 3, 4, 5]) == 9
    assert largest_rectangle_area([5, 4, 3, 2, 1]) == 9
    # Edge cases: empty, single bar, all zeroes
    assert largest_rectangle_area([]) == 0
    assert largest_rectangle_area([7]) == 7
    assert largest_rectangle_area([0, 0, 0]) == 0
    try:
        largest_rectangle_area([2, -1])
    except ValueError:
        pass
    else:
        raise AssertionError("negative height must raise ValueError")
    print("largest_rectangle_in_histogram: OK")
