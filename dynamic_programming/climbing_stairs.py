"""
Problem: Climbing Stairs
You climb 1 or 2 steps at a time. How many distinct ways reach step n?
Example: n=3 -> 3  (1+1+1, 1+2, 2+1)

Approach: Dynamic programming. ways(n) = ways(n-1) + ways(n-2) - the
Fibonacci recurrence. Only the last two values are needed, so space is
constant.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def climb_stairs(n: int) -> int:
    """Return the number of distinct ways to climb ``n`` steps."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 2:
        return max(n, 1)
    prev, curr = 1, 2  # ways(1), ways(2)
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    print("climbing_stairs: OK")
