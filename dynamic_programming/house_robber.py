"""
Problem: House Robber
Houses in a row hold amounts of money. Robbing two adjacent houses
triggers an alarm. Return the maximum amount that can be taken.
Example: [2,7,9,3,1] -> 12  (2 + 9 + 1)

Approach: DP with two states rolling forward: for each house, the best
total either skips it (previous best) or takes it (best from two houses
back + this house). Keep only the last two values.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def rob(nums: list[int]) -> int:
    """Return the maximum loot without robbing adjacent houses."""
    rob_prev = 0   # best up to two houses ago
    rob_curr = 0   # best up to previous house
    for value in nums:
        rob_prev, rob_curr = rob_curr, max(rob_curr, rob_prev + value)
    return rob_curr


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    print("house_robber: OK")
