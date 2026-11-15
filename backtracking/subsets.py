"""
Problem: Subsets
Given a list of distinct integers, return all possible subsets (the
power set). The solution set must not contain duplicate subsets, and
the subsets may be returned in any order.
Example: [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]];
[0] -> [[],[0]]

Approach: Depth-first backtracking over a start index. At each call,
record a copy of the current subset, then try appending each remaining
element in turn, recurse past it, and undo the append. Because each
element is either taken once in index order or skipped, every one of
the 2^n subsets is produced exactly once, with no duplicates, and
elements always appear in their input order inside a subset. The
input list is never mutated.

Time Complexity: O(n * 2^n) — 2^n subsets, each copied in O(n)
Space Complexity: O(n) recursion depth, excluding the output
"""

from __future__ import annotations


def subsets(nums: list[int]) -> list[list[int]]:
    """Return all subsets of the distinct values in ``nums``."""
    results: list[list[int]] = []
    current: list[int] = []

    def backtrack(start: int) -> None:
        results.append(list(current))
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return results


if __name__ == "__main__":
    assert subsets([1, 2, 3]) == [
        [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3],
    ]
    assert subsets([0]) == [[], [0]]
    # Count check: n distinct values give exactly 2^n subsets
    assert len(subsets([1, 2, 3, 4])) == 16
    # Edge cases: empty input has only the empty subset, single element
    assert subsets([]) == [[]]
    assert subsets([5]) == [[], [5]]
    # Input must not be mutated
    data = [2, 1]
    assert subsets(data) == [[], [2], [2, 1], [1]]
    assert data == [2, 1]
    print("subsets: OK")
