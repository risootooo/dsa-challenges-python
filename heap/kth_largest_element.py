"""
Problem: Kth Largest Element in an Array
Find the k-th largest element (in sorted order, not the k-th distinct).
Example: [3,2,1,5,6,4], k=2 -> 5

Approach: Maintain a min-heap of size k holding the k largest elements
seen so far. The top of the heap is then the k-th largest. This beats
fully sorting when k is small, and streams naturally.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

from __future__ import annotations

import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    """Return the k-th largest element of ``nums``."""
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    heap: list[int] = []
    for value in nums:
        heapq.heappush(heap, value)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    print("kth_largest_element: OK")
