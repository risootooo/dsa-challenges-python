"""
Problem: Rotting Oranges
A grid holds 0 (empty), 1 (fresh orange) or 2 (rotten orange). Every
minute, each fresh orange adjacent (up/down/left/right) to a rotten one
becomes rotten. Return the minutes until no fresh orange remains, or -1
if some fresh orange can never rot.
Example: [[2,1,1],[1,1,0],[0,1,1]] -> 4; [[0,2]] -> 0

Approach: Multi-source BFS. Seed the queue with every initially rotten
orange at time 0, then expand level by level: a fresh orange reached at
level t rots at minute t. Counting levels (not individual oranges)
gives elapsed minutes. If any fresh orange is never reached, it is
unreachable and the answer is -1. A separate visited set is used so the
input grid is never mutated.

Time Complexity: O(rows * cols)
Space Complexity: O(rows * cols)
"""

from __future__ import annotations

from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    """Minutes until all oranges rot, or -1 if that is impossible."""
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    queue: deque[tuple[int, int]] = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    if fresh == 0:
        return 0

    visited: set[tuple[int, int]] = set(queue)
    minutes = 0
    while queue and fresh > 0:
        minutes += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == 1
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    fresh -= 1
    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert oranges_rotting(grid) == 4
    assert grid == [[2, 1, 1], [1, 1, 0], [0, 1, 1]]  # input untouched
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
    assert oranges_rotting([[1]]) == -1
    assert oranges_rotting([[2]]) == 0
    assert oranges_rotting([]) == 0
    print("rotting_oranges: OK")
