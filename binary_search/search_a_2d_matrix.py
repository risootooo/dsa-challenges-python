"""
Problem: Search a 2D Matrix
Search for a target in an m x n matrix where each row is sorted in
ascending order and the first element of each row is greater than
the last element of the previous row. Return True if present.
Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> True

Approach: Because the rows join into one globally sorted sequence,
treat the matrix as a flattened sorted array of length m * n and run
a plain binary search, mapping a flat index back to (row, col) with
divmod by the column count.

Time Complexity: O(log(m * n))
Space Complexity: O(1)
"""

from __future__ import annotations


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    """Return True if ``target`` occurs in the sorted ``matrix``."""
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        row, col = divmod(mid, cols)
        value = matrix[row][col]
        if value == target:
            return True
        if value < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


if __name__ == "__main__":
    grid = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(grid, 3) is True
    assert search_matrix(grid, 13) is False
    assert search_matrix([], 1) is False
    print("search_a_2d_matrix: OK")
