"""
Problem: Combination Sum
Given distinct positive integers (candidates) and a target, return
all unique combinations of the candidates that sum to the target.
The same candidate may be chosen any number of times; two
combinations are the same if they use each value the same number
of times.
Example: candidates [2,3,6,7], target 7 -> [[2,2,3],[7]];
candidates [2,3,5], target 8 -> [[2,2,2,2],[2,3,3],[3,5]]

Approach: Depth-first backtracking over the candidates in sorted
order. At each step, either take the candidate at the current index
again (it stays available, since reuse is unlimited) or move on to
the next index. Carrying a start index — never looking backwards —
is what guarantees each multiset is generated exactly once, in
non-decreasing order. Branches prune as soon as the running sum
would exceed the target, which the sorted order makes safe: every
later candidate is at least as large.

Time Complexity: O(N^(T/M)) worst case, N = candidates, T = target,
M = smallest candidate (bounded by the number of valid combinations)
Space Complexity: O(T/M) recursion depth, excluding the output
"""

from __future__ import annotations


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """All unique combinations of ``candidates`` summing to ``target``."""
    if target < 0:
        return []
    if target == 0:
        return [[]]
    ordered = sorted(c for c in candidates if c > 0)
    results: list[list[int]] = []
    current: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            results.append(list(current))
            return
        for i in range(start, len(ordered)):
            value = ordered[i]
            if value > remaining:
                break
            current.append(value)
            backtrack(i, remaining - value)
            current.pop()

    backtrack(0, target)
    return results


if __name__ == "__main__":
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    # Order of the input does not change the combinations produced
    assert combination_sum([7, 2, 6, 3], 7) == [[2, 2, 3], [7]]
    # No-solution and edge cases
    assert combination_sum([2], 1) == []
    assert combination_sum([5], 5) == [[5]]
    assert combination_sum([], 5) == []
    assert combination_sum([2, 3], 0) == [[]]
    print("combination_sum: OK")
