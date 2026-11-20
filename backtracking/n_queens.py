"""
Problem: N-Queens
Place n queens on an n x n chessboard so that no two queens attack
each other (no shared row, column or diagonal). Return all distinct
solutions, each as a list of n strings with 'Q' for a queen and '.'
for an empty square.
Example: n=4 -> [[".Q..","...Q","Q...","..Q."],
["..Q.","Q...","...Q",".Q.."]]; n=1 -> [["Q"]]

Approach: Depth-first backtracking row by row. Exactly one queen
must sit in each row, so the search only chooses its column. Three
sets record the columns and both diagonals (identified by r-c and
r+c) already under attack, which makes each placement check O(1)
and prunes any partial board that can never complete. When row n is
reached the accumulated rows form one solution. For n <= 0 there are
no solutions, so the result is an empty list.

Time Complexity: O(n!) worst case — pruned by the attack sets
Space Complexity: O(n) recursion depth and attack sets, excluding
the output
"""

from __future__ import annotations


def solve_n_queens(n: int) -> list[list[str]]:
    """Return every solution to the n-queens puzzle."""
    if n <= 0:
        return []
    solutions: list[list[str]] = []
    board: list[str] = []
    columns: set[int] = set()
    diag_down: set[int] = set()  # r - c is constant along a \ diagonal
    diag_up: set[int] = set()  # r + c is constant along a / diagonal

    def backtrack(row: int) -> None:
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if col in columns or (row - col) in diag_down or (row + col) in diag_up:
                continue
            columns.add(col)
            diag_down.add(row - col)
            diag_up.add(row + col)
            board.append("." * col + "Q" + "." * (n - col - 1))
            backtrack(row + 1)
            board.pop()
            columns.remove(col)
            diag_down.remove(row - col)
            diag_up.remove(row + col)

    backtrack(0)
    return solutions


if __name__ == "__main__":
    assert solve_n_queens(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert solve_n_queens(1) == [["Q"]]
    # No solutions exist for 2 or 3 queens
    assert solve_n_queens(2) == []
    assert solve_n_queens(3) == []
    # Known solution counts (OEIS A000170)
    assert len(solve_n_queens(5)) == 10
    assert len(solve_n_queens(6)) == 4
    # Edge cases: degenerate board sizes
    assert solve_n_queens(0) == []
    assert solve_n_queens(-3) == []
    print("n_queens: OK")
