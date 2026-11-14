"""
Problem: Set Matrix Zeroes
Given an m x n matrix, if an element is 0, set its entire row and
column to 0. Do it in place.
Example: [[1,1,1],[1,0,1],[1,1,1]] -> [[1,0,1],[0,0,0],[1,0,1]];
[[0,1,2,0],[3,4,5,2],[1,3,1,5]] -> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Approach: Use the first row and first column as the marker storage
instead of allocating two marker arrays. First record separately
whether the first row and the first column themselves contain a zero,
because their cells double as markers and would otherwise lose that
information. Scan the interior: a zero at (i, j) marks matrix[i][0]
and matrix[0][j]. Then zero every interior cell whose row or column
marker is set. Finally apply the two saved flags to the first row and
column themselves. An empty matrix is already done.

Time Complexity: O(m*n)
Space Complexity: O(1) extra
"""

from __future__ import annotations


def set_zeroes(matrix: list[list[int]]) -> None:
    """Zero the full row and column of every zero in ``matrix``, in place."""
    if not matrix or not matrix[0]:
        return
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
    # Mark rows/columns that contain a zero, using the first row/col.
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # Zero interior cells from the markers.
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # Zero the first row and column themselves, from the saved flags
    # and the markers left in them.
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


if __name__ == "__main__":
    data = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(data)
    assert data == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    larger = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(larger)
    assert larger == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    # No zeroes: matrix is unchanged
    clean = [[1, 2], [3, 4]]
    set_zeroes(clean)
    assert clean == [[1, 2], [3, 4]]
    # Zero in the first row / first column only
    edge = [[0, 2], [3, 4]]
    set_zeroes(edge)
    assert edge == [[0, 0], [0, 4]]
    # Edge cases: empty matrix, single cell (zero and non-zero)
    empty: list[list[int]] = []
    set_zeroes(empty)
    assert empty == []
    single = [[0]]
    set_zeroes(single)
    assert single == [[0]]
    one = [[5]]
    set_zeroes(one)
    assert one == [[5]]
    print("set_matrix_zeroes: OK")
