"""
Problem: Longest Increasing Subsequence
Return the length of the longest strictly increasing subsequence (not
necessarily contiguous) of an array.
Example: [10,9,2,5,3,7,101,18] -> 4  (e.g. [2,3,7,101])

Approach: Patience sorting. tails[i] is the smallest possible tail value of
any increasing subsequence of length i+1 seen so far. For each x, binary
search (bisect_left) finds the first tail >= x and replaces it: extending a
subsequence when x belongs at the end, or improving (lowering) the tail of
an existing length so future elements have more room. len(tails) is the
answer. The classic O(n^2) DP is included for comparison/teaching.

Time Complexity: O(n log n) for length_of_lis; O(n^2) for length_of_lis_dp
Space Complexity: O(n)
"""

from __future__ import annotations

from bisect import bisect_left


def length_of_lis(nums: list[int]) -> int:
    """Length of the longest strictly increasing subsequence, O(n log n)."""
    tails: list[int] = []
    for x in nums:
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
    return len(tails)


def length_of_lis_dp(nums: list[int]) -> int:
    """Length of the longest increasing subsequence, classic O(n^2) DP."""
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7, 7]) == 1
    assert length_of_lis([]) == 0
    assert length_of_lis_dp([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print("longest_increasing_subsequence: OK")
