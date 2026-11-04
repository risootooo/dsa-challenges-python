"""
Problem: Rotate Array
Rotate an array to the right by k steps, in place.
Example: [1, 2, 3, 4, 5, 6, 7], k=3 -> [5, 6, 7, 1, 2, 3, 4]

Approach: Reverse the whole array, then reverse the first k elements and
the remaining n-k elements. Three reversals achieve the rotation in place.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def rotate(nums: list[int], k: int) -> None:
    """Rotate ``nums`` right by ``k`` steps, modifying it in place."""
    if not nums:
        return
    n = len(nums)
    k %= n

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7]
    rotate(data, 3)
    assert data == [5, 6, 7, 1, 2, 3, 4]
    print("rotate_array: OK")
