"""
Problem: Sliding Window Maximum
Given an array and a window size k, return the maximum of every contiguous
window of size k as the window slides one step at a time.
Example: nums=[1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]

Approach: Monotonic deque of indices whose values are strictly decreasing.
Before adding index i, evict indices that fell out of the window from the
front and pop smaller-or-equal values from the back (they can never be a
window maximum while i is present). The deque front is always the current
window's maximum. Each index enters and leaves the deque once.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from __future__ import annotations

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Return the maximum of each size-k sliding window over `nums`."""
    if not nums or k <= 0:
        return []
    window: deque[int] = deque()  # indices, values strictly decreasing
    result: list[int] = []
    for i, value in enumerate(nums):
        while window and window[0] <= i - k:
            window.popleft()  # out of the window
        while window and nums[window[-1]] <= value:
            window.pop()  # dominated by the new value
        window.append(i)
        if i >= k - 1:
            result.append(nums[window[0]])
    return result


if __name__ == "__main__":
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([9, 8, 7, 6], 2) == [9, 8, 7]
    print("sliding_window_maximum: OK")
