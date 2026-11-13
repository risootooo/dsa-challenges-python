"""
Problem: Rotate Image
Given an n x n matrix, rotate it by 90 degrees clockwise, in place.
Example: [[1,2,3],[4,5,6],[7,8,9]] -> [[7,4,1],[8,5,2],[9,6,3]];
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] ->
[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Approach: A 90-degree clockwise rotation is a transpose followed by
reversing each row. Transposing swaps matrix[i][j] with matrix[j][i]
across the main diagonal, which turns columns into rows; reversing
each row then puts those rows in clockwise order. Both steps are
in place, so no second matrix is allocated. An empty matrix and a
1 x 1 matrix are already rotated.

Time Complexity: O(n^2)
Space Complexity: O(1) extra
"""

from __future__ import annotations


def rotate_image(matrix: list[list[int]]) -> None:
    """Rotate the square ``matrix`` 90 degrees clockwise, in place."""
    n = len(matrix)
    if n <= 1:
        return
    # Transpose: swap across the main diagonal.
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row.
    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_image(data)
    assert data == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    larger = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate_image(larger)
    assert larger == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    # Rotating four times restores the original matrix
    spun = [[1, 2], [3, 4]]
    for _ in range(4):
        rotate_image(spun)
    assert spun == [[1, 2], [3, 4]]
    # Edge cases: empty matrix, single cell, single row of one cell
    empty: list[list[int]] = []
    rotate_image(empty)
    assert empty == []
    single = [[1]]
    rotate_image(single)
    assert single == [[1]]
    print("rotate_image: OK")
