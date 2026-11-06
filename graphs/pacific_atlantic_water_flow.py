"""
Problem: Pacific Atlantic Water Flow
An m x n island is bordered by the Pacific Ocean (top and left edges)
and the Atlantic Ocean (bottom and right edges). Water at a cell can
flow to a neighbouring cell (up/down/left/right) whose height is less
than or equal to its own. Return the cells from which rain water can
reach BOTH oceans.
Example: [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
-> [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Approach: Reverse the flow. Instead of flowing downhill from every
cell, start from each ocean's border and walk uphill: a cell reached
from the Pacific border can drain to the Pacific, because every step
of the reverse walk goes to a cell at least as high, so water flows
back down along the same path. Run this DFS once from the Pacific
edges and once from the Atlantic edges; the answer is the set of
cells reached by both walks.

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)
"""

from __future__ import annotations


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    """Cells (as [row, col] lists) whose water reaches both oceans."""
    if not heights or not heights[0]:
        return []
    rows, cols = len(heights), len(heights[0])

    def reachable(starts: list[tuple[int, int]]) -> set[tuple[int, int]]:
        seen: set[tuple[int, int]] = set(starts)
        stack = list(starts)
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in seen
                    and heights[nr][nc] >= heights[r][c]
                ):
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        return seen

    pacific = reachable(
        [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
    )
    atlantic = reachable(
        [(r, cols - 1) for r in range(rows)]
        + [(rows - 1, c) for c in range(cols)]
    )
    return [[r, c] for r, c in sorted(pacific & atlantic)]


if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    assert pacific_atlantic(heights) == [
        [0, 4],
        [1, 3],
        [1, 4],
        [2, 2],
        [3, 0],
        [3, 1],
        [4, 0],
    ]
    assert pacific_atlantic([[1]]) == [[0, 0]]
    assert pacific_atlantic([[1, 1], [1, 1]]) == [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert pacific_atlantic([]) == []
    assert pacific_atlantic([[]]) == []
    print("pacific_atlantic_water_flow: OK")
