"""
Problem: Koko Eating Bananas
Koko has piles of bananas, piles[i] in pile i. Guards return in h hours.
Each hour she chooses one pile and eats up to k bananas from it (fewer
if the pile is smaller). Find the minimum integer eating speed k such
that she can eat all the bananas within h hours.
Example: piles=[3,6,7,11], h=8 -> 4; piles=[30,11,23,4,20], h=5 -> 30;
piles=[30,11,23,4,20], h=6 -> 23

Approach: Binary search on the answer. Feasibility is monotone in k:
if speed k finishes within h hours, every faster speed does too, and
if k is too slow, every slower speed is too. So search k in
[1, max(piles)] for the smallest feasible value. The hours needed at
speed k are the sum over piles of ceil(pile / k), computed with integer
arithmetic as (pile + k - 1) // k. When h is smaller than the number of
piles no speed can finish (each pile takes at least one hour), so the
function returns -1; an empty pile list needs no hours and returns 0.

Time Complexity: O(n * log(max(piles))) — feasibility check is O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def _hours_needed(piles: list[int], k: int) -> int:
    """Hours to finish ``piles`` eating at most ``k`` bananas per hour."""
    return sum((pile + k - 1) // k for pile in piles)


def min_eating_speed(piles: list[int], h: int) -> int:
    """Return the minimum speed finishing ``piles`` within ``h`` hours.

    Returns 0 for an empty pile list and -1 when finishing is
    impossible because ``h`` is smaller than the number of piles.
    """
    if not piles:
        return 0
    if h < len(piles):
        return -1
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if _hours_needed(piles, mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1, 1, 1, 999999999], 10) == 142857143
    # Edge cases: empty input, single pile, no-solution
    assert min_eating_speed([], 5) == 0
    assert min_eating_speed([5], 5) == 1
    assert min_eating_speed([5], 1) == 5
    assert min_eating_speed([3, 6, 7, 11], 3) == -1
    print("koko_eating_bananas: OK")
