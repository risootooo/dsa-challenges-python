"""
Problem: Coin Change
Given coin denominations and an amount, return the fewest coins needed
to make the amount, or -1 if impossible.
Example: coins=[1,2,5], amount=11 -> 3  (5 + 5 + 1)

Approach: Bottom-up DP. dp[x] is the fewest coins for amount x. For each
amount, try every coin that fits and take 1 + dp[x - coin] at its best.

Time Complexity: O(amount * number_of_coins)
Space Complexity: O(amount)
"""

from __future__ import annotations


def coin_change(coins: list[int], amount: int) -> int:
    """Return the minimum number of coins to make ``amount``, or -1."""
    if amount < 0:
        return -1
    unreachable = amount + 1
    dp = [unreachable] * (amount + 1)
    dp[0] = 0
    for x in range(1, amount + 1):
        for coin in coins:
            if coin <= x:
                dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != unreachable else -1


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    print("coin_change: OK")
