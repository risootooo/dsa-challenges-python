"""
Problem: Partition Equal Subset Sum
Given a list of positive integers, return True if the list can be
partitioned into two subsets with equal sum, and False otherwise.
Example: [1,5,11,5] -> True ([1,5,5] and [11]);
[1,2,3,5] -> False

Approach: If the total sum is odd, no equal partition exists. Otherwise
the question is whether some subset sums to total // 2 — a 0/1
knapsack / subset-sum problem. Keep a boolean array reachable[s] for
sums up to the target, with reachable[0] = True, and for each value
update sums in DESCENDING order: reachable[s] = reachable[s] or
reachable[s - value]. Descending is the whole trick — it guarantees
each value is used at most once, because reachable[s - value] still
reflects the state before this value. Ascending order would allow
reusing the same value unlimited times.

Time Complexity: O(n * target), where target = sum(nums) // 2
Space Complexity: O(target)
"""

from __future__ import annotations


def can_partition(nums: list[int]) -> bool:
    """Return True if ``nums`` splits into two subsets of equal sum."""
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    reachable = [False] * (target + 1)
    reachable[0] = True
    for value in nums:
        for s in range(target, value - 1, -1):
            if reachable[s - value]:
                reachable[s] = True
        if reachable[target]:
            return True
    return reachable[target]


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([1, 2, 5]) is False
    assert can_partition([2, 2, 3, 5]) is False
    assert can_partition([3, 3, 3, 4, 5]) is True
    # Edge cases: empty input, single element, two equal elements
    assert can_partition([]) is True
    assert can_partition([100]) is False
    assert can_partition([1, 1]) is True
    assert can_partition([2, 2]) is True
    # Odd total can never be partitioned, however the values are arranged
    assert can_partition([1, 2, 4]) is False
    print("partition_equal_subset_sum: OK")
