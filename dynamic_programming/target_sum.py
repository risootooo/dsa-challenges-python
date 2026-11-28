"""
Problem: Target Sum
Given an integer array nums and an integer target, return the number
of expressions built by inserting '+' or '-' before every element of
nums (each element used exactly once, in order) whose value equals
target.
Example: nums=[1,1,1,1,1], target=3 -> 5; nums=[1], target=1 -> 1

Approach: DP over reachable sums. A dictionary maps each sum that can
be formed from the processed prefix to the number of sign assignments
producing it; each new number branches every entry into sum + num and
sum - num, adding the counts. Sums stay within [-total, total], so the
dictionary holds at most 2 * total + 1 entries. Equivalently, choosing
the '+' subset P and '-' subset N needs sum(P) - sum(N) = target with
sum(P) + sum(N) = total, i.e. sum(P) = (total + target) / 2 — the DP
counts those assignments directly without enumerating subsets.

Time Complexity: O(n * total), total = sum(nums)
Space Complexity: O(total) for the reachable-sums dictionary
"""

from __future__ import annotations


def find_target_sum_ways(nums: list[int], target: int) -> int:
    """Return the number of +/- assignments to ``nums`` equal to
    ``target``.

    The empty list has exactly one assignment (the empty expression),
    which reaches only target 0.
    """
    ways: dict[int, int] = {0: 1}
    for num in nums:
        next_ways: dict[int, int] = {}
        for total, count in ways.items():
            next_ways[total + num] = next_ways.get(total + num, 0) + count
            next_ways[total - num] = next_ways.get(total - num, 0) + count
        ways = next_ways
    return ways.get(target, 0)


if __name__ == "__main__":
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5
    assert find_target_sum_ways([1], 1) == 1
    assert find_target_sum_ways([1], 0) == 0
    assert find_target_sum_ways([1, 2, 3], 0) == 2  # 1+2-3, -1-2+3
    # Zeros double the count: each 0 may take either sign freely
    assert find_target_sum_ways([0, 0, 1], 1) == 4
    # Edge cases: empty input, single element, unreachable target
    assert find_target_sum_ways([], 0) == 1
    assert find_target_sum_ways([], 5) == 0
    assert find_target_sum_ways([2], -2) == 1
    assert find_target_sum_ways([1, 2], 10) == 0
    # Parity: total and target must share parity to be reachable
    assert find_target_sum_ways([1, 2], 2) == 0
    print("target_sum: OK")
