"""
Problem: Flood Fill
Starting from a pixel, change its colour - and every connected pixel of
the same original colour (4-directionally) - to a new colour.
Example: image [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, colour=2
         -> [[2,2,2],[2,2,0],[2,0,1]]

Approach: Iterative DFS with an explicit stack. Only traverse pixels that
still hold the starting colour, which both bounds the fill and prevents
infinite loops when the new colour equals the old one.

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols) worst case
"""

from __future__ import annotations


def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    """Return a new image flood-filled from (sr, sc) with ``color``."""
    result = [row[:] for row in image]
    start_color = image[sr][sc]
    if start_color == color:
        return result
    rows, cols = len(image), len(image[0])
    stack = [(sr, sc)]
    result[sr][sc] = color
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and result[nr][nc] == start_color:
                result[nr][nc] = color
                stack.append((nr, nc))
    return result


if __name__ == "__main__":
    assert flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    print("flood_fill: OK")
