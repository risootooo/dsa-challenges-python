"""
Problem: Surrounded Regions
Given an m x n board of 'X' and 'O', capture every region of 'O's
that is surrounded by 'X's on all four sides: an 'O' region flips to
'X' unless it touches the border, in which case it (and everything
connected to it) survives. Return the board after capture, as a new
board; the input is not mutated.
Example: [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],
["X","O","X","X"]] -> [["X","X","X","X"],["X","X","X","X"],
["X","X","X","X"],["X","O","X","X"]]

Approach: Work backwards from survival instead of capture. Flood
fill (DFS) from every border 'O' and mark the cells reached: those
regions touch the border, so they survive. Every 'O' left unmarked
is fully surrounded and flips to 'X'; marked cells stay 'O'.

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)
"""

from __future__ import annotations


def solve(board: list[list[str]]) -> list[list[str]]:
    """Board after capturing surrounded 'O' regions (new board)."""
    if not board or not board[0]:
        return [row[:] for row in board]
    rows, cols = len(board), len(board[0])
    result = [row[:] for row in board]
    safe: set[tuple[int, int]] = set()
    stack: list[tuple[int, int]] = []
    for r in range(rows):
        for c in (0, cols - 1):
            if result[r][c] == "O" and (r, c) not in safe:
                safe.add((r, c))
                stack.append((r, c))
    for c in range(cols):
        for r in (0, rows - 1):
            if result[r][c] == "O" and (r, c) not in safe:
                safe.add((r, c))
                stack.append((r, c))
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in safe
                and result[nr][nc] == "O"
            ):
                safe.add((nr, nc))
                stack.append((nr, nc))
    for r in range(rows):
        for c in range(cols):
            if result[r][c] == "O" and (r, c) not in safe:
                result[r][c] = "X"
    return result


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    assert solve(board) == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    assert board[1][1] == "O"  # input not mutated
    assert solve([["O"]]) == [["O"]]
    assert solve([["X"]]) == [["X"]]
    assert solve([]) == []
    assert solve([[]]) == [[]]
    assert solve([["O", "O"], ["O", "O"]]) == [["O", "O"], ["O", "O"]]
    print("surrounded_regions: OK")
