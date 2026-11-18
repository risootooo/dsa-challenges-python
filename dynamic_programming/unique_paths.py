"""
Problem: Unique Paths
A robot starts at the top-left corner of an m x n grid and wants to
reach the bottom-right corner, moving only right or down. Return how
many distinct paths exist.
Example: m=3, n=7 -> 28; m=3, n=2 -> 3; m=1, n=1 -> 1

Approach: Dynamic programming over one row. Every cell is reached
either from the cell above it or from the cell to its left, so its
path count is the sum of those two counts. The first row and the first
column each have exactly one path (all moves in a single direction).
Keeping only the current row suffices: dp[j] still holds the count
from above until it is updated with the count from the left in the
same pass. A grid with a non-positive dimension has no paths.

Time Complexity: O(m * n)
Space Complexity: O(n)
"""

from __future__ import annotations


def unique_paths(m: int, n: int) -> int:
    """Return the number of right/down-only paths across an m x n grid."""
    if m <= 0 or n <= 0:
        return 0
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


if __name__ == "__main__":
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(3, 3) == 6
    assert unique_paths(7, 3) == 28
    # Edge cases: single cell, single row/column, degenerate grids
    assert unique_paths(1, 1) == 1
    assert unique_paths(1, 10) == 1
    assert unique_paths(10, 1) == 1
    assert unique_paths(0, 5) == 0
    assert unique_paths(5, 0) == 0
    assert unique_paths(-2, 3) == 0
    print("unique_paths: OK")
