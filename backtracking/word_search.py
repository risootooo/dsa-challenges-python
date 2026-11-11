"""
Problem: Word Search
Given a board of characters and a word, determine whether the word
exists in the grid. The word can be constructed from letters of
sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighbouring. The same letter cell may not be used
more than once in a word.
Example: board [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
with "ABCCED" -> True; with "SEE" -> True; with "ABCB" -> False

Approach: Depth-first backtracking from every cell that matches the
first character. At each step the current cell is marked as visited,
the four orthogonal neighbours are tried for the next character, and
the mark is undone on return so other paths can reuse the cell. A
cell matches only when its character equals the character needed at
that position, so a path succeeds exactly when it consumes the whole
word. The board is restored to its original contents before return.

Time Complexity: O(rows * cols * 4^L) worst case, L = len(word)
Space Complexity: O(L) recursion depth
"""

from __future__ import annotations


def exist(board: list[list[str]], word: str) -> bool:
    """Return True if ``word`` can be traced through adjacent cells in ``board``."""
    if not board or not board[0] or not word:
        return False
    rows, cols = len(board), len(board[0])
    if len(word) > rows * cols:
        return False

    def backtrack(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if board[r][c] != word[index]:
            return False
        saved = board[r][c]
        board[r][c] = "#"
        try:
            return (
                backtrack(r + 1, c, index + 1)
                or backtrack(r - 1, c, index + 1)
                or backtrack(r, c + 1, index + 1)
                or backtrack(r, c - 1, index + 1)
            )
        finally:
            board[r][c] = saved

    return any(
        backtrack(r, c, 0)
        for r in range(rows)
        for c in range(cols)
        if board[r][c] == word[0]
    )


if __name__ == "__main__":
    sample = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert exist([row[:] for row in sample], "ABCCED") is True
    assert exist([row[:] for row in sample], "SEE") is True
    # No-solution: a cell cannot be reused within one word
    assert exist([row[:] for row in sample], "ABCB") is False
    # Board is restored after the search
    board = [row[:] for row in sample]
    exist(board, "ABCCED")
    assert board == sample
    # Edge cases: single cell, empty board, empty word, word longer than grid
    assert exist([["a"]], "a") is True
    assert exist([["a"]], "b") is False
    assert exist([], "a") is False
    assert exist([[]], "a") is False
    assert exist([["a"]], "") is False
    assert exist([["a", "b"]], "abc") is False
    print("word_search: OK")
