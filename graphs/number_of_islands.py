"""
Problem: Number of Islands
Given a grid of "1" (land) and "0" (water), count islands - groups of
land connected horizontally or vertically.
Example: grid with three separate land masses -> 3

Approach: Scan the grid. Each time unvisited land is found, increment the
count and flood-fill (DFS) the whole island, marking cells visited so it
is counted only once.

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols) worst case for the recursion / visited set
"""

from __future__ import annotations


def num_islands(grid: list[list[str]]) -> int:
    """Count islands in a binary grid without mutating the input."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()

    def dfs(r: int, c: int) -> None:
        stack = [(r, c)]
        visited.add((r, c))
        while stack:
            cr, cc = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    stack.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                dfs(r, c)
    return count


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(grid) == 3
    print("number_of_islands: OK")
