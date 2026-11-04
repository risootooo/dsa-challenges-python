"""
Problem: 0/1 Knapsack
Given items each with a weight and a value, and a knapsack of fixed
capacity, return the maximum total value that fits. Each item may be taken
at most once (0/1).
Example: weights=[1,3,4,5], values=[1,4,5,7], capacity=7 -> 9 (items 3+4)

Approach: dp[w] = best value achievable with capacity w using the items
processed so far. For each item, update capacities in DESCENDING order:
dp[w] = max(dp[w], dp[w - weight] + value). Descending is the whole trick —
it guarantees the item is counted at most once, because dp[w - weight] still
reflects the state before this item. Ascending order would solve the
unbounded knapsack instead.

Time Complexity: O(n * capacity)
Space Complexity: O(capacity)
"""

from __future__ import annotations


def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """Return the maximum value fitting in the knapsack (each item once)."""
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    dp = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[capacity]


if __name__ == "__main__":
    assert knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
    assert knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
    assert knapsack([], [], 10) == 0
    assert knapsack([10], [100], 5) == 0
    print("knapsack_01: OK")
