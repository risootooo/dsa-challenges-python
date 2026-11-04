"""
Problem: Top K Frequent Elements
Return the k most frequent elements of an array, in any order.
Example: [1,1,1,2,2,3], k=2 -> [1, 2]

Approach: Count frequencies, then use a bucket indexed by frequency
(bucket sort on counts). Scanning buckets from high to low yields the
top k in linear time, avoiding a full sort of distinct elements.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations

from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the ``k`` most frequent elements (any order)."""
    counts = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)
    result: list[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for value in buckets[freq]:
            result.append(value)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert top_k_frequent([1], 1) == [1]
    print("top_k_frequent_elements: OK")
