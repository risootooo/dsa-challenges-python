"""
Problem: Permutations
Given a list of distinct integers, return all possible permutations
of the list in any order.
Example: [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]];
[0,1] -> [[0,1],[1,0]]; [1] -> [[1]]

Approach: Depth-first backtracking with a used-flag for each index.
At each position, try every still-unused element, append it, recurse
to fill the next position, then undo both the append and the flag.
Because the input values are distinct, tracking usage by index is
enough to produce each of the n! orderings exactly once, in the
lexicographic order induced by the input order. The input list is
never mutated.

Time Complexity: O(n * n!) — n! permutations, each copied in O(n)
Space Complexity: O(n) recursion depth and used-flags, excluding the output
"""

from __future__ import annotations


def permute(nums: list[int]) -> list[list[int]]:
    """Return all permutations of the distinct values in ``nums``."""
    results: list[list[int]] = []
    current: list[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(current) == len(nums):
            results.append(list(current))
            return
        for i, value in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            current.append(value)
            backtrack()
            current.pop()
            used[i] = False

    backtrack()
    return results


if __name__ == "__main__":
    assert permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert permute([0, 1]) == [[0, 1], [1, 0]]
    # Edge cases: single element, empty input
    assert permute([1]) == [[1]]
    assert permute([]) == [[]]
    # Input order drives output order; input itself is not mutated
    data = [2, 1]
    assert permute(data) == [[2, 1], [1, 2]]
    assert data == [2, 1]
    print("permutations: OK")
