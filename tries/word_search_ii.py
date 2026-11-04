"""
Problem: Word Search II
Given an m x n board of characters and a list of words, return every word
that can be formed by sequentially adjacent (horizontal/vertical) cells
without reusing a cell within one word.
Example: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],
                  ["i","f","l","v"]],
         words = ["oath","pea","eat","rain"] -> ["oath","eat"] (order-free)

Approach: Insert all words into a trie, then DFS from each cell, walking the
board and the trie together. A board path that is not a trie prefix is pruned
immediately, which is what makes this tractable — the naive approach (a full
board search per word) multiplies the board scan by the word count. Matched
words are removed from the trie so each is reported once.

Time Complexity: O(m * n * 4^L) worst case, L = longest word; trie pruning
                 makes the practical cost far lower
Space Complexity: O(total word characters) for the trie + O(L) recursion
"""

from __future__ import annotations


class _TrieNode:
    __slots__ = ("children", "word")

    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.word: str | None = None  # set at the node ending a dictionary word


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    """Return the subset of `words` that can be traced on `board`."""
    if not board or not board[0] or not words:
        return []

    root = _TrieNode()
    for word in words:
        node = root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        node.word = word

    rows, cols = len(board), len(board[0])
    found: list[str] = []

    def dfs(r: int, c: int, node: _TrieNode) -> None:
        ch = board[r][c]
        child = node.children.get(ch)
        if child is None:
            return
        if child.word is not None:
            found.append(child.word)
            child.word = None  # report each word once
        board[r][c] = "#"  # mark visited
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, child)
        board[r][c] = ch  # restore

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return found


if __name__ == "__main__":
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    result = find_words([row[:] for row in board], ["oath", "pea", "eat", "rain"])
    assert sorted(result) == ["eat", "oath"]
    print("word_search_ii: OK")
