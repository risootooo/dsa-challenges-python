"""
Problem: Spiral Matrix
Given an m x n matrix, return all its elements in spiral order —
starting at the top-left, moving right across the top row, down the
right column, left across the bottom row, up the left column, and
repeating inward until every element has been visited exactly once.
Example: [[1,2,3],[4,5,6],[7,8,9]] -> [1,2,3,6,9,8,7,4,5];
[[1,2,3,4],[5,6,7,8],[9,10,11,12]] -> [1,2,3,4,8,12,11,10,9,5,6,7]

Approach: Keep four boundaries — top, bottom, left and right — that
frame the not-yet-visited sub-matrix. Walk the top row left to right
and move top down, walk the right column top to bottom and move right
in, walk the bottom row right to left (only if a row remains) and move
bottom up, then walk the left column bottom to top (only if a column
remains) and move left in. The guards before the bottom and left
passes stop a single remaining row or column being read twice. The
input is only read, never mutated.

Time Complexity: O(m*n)
Space Complexity: O(1) extra (excluding the output list)
"""

from __future__ import annotations


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return the elements of ``matrix`` in clockwise spiral order."""
    if not matrix or not matrix[0]:
        return []
    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result


if __name__ == "__main__":
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7,
    ]
    # Rectangular and degenerate shapes
    assert spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert spiral_order([[1, 2, 3]]) == [1, 2, 3]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
    # Edge cases: empty matrix, empty row, single cell
    assert spiral_order([]) == []
    assert spiral_order([[]]) == []
    assert spiral_order([[7]]) == [7]
    # Input must not be mutated
    data = [[1, 2], [3, 4]]
    spiral_order(data)
    assert data == [[1, 2], [3, 4]]
    print("spiral_matrix: OK")
