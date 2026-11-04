"""
Problem: Best Time to Buy and Sell Stock
Given daily prices, choose one day to buy and a later day to sell to
maximise profit. Return 0 if no profit is possible.
Example: [7, 1, 5, 3, 6, 4] -> 5  (buy at 1, sell at 6)

Approach: One pass. Track the lowest price seen so far and the best profit
from selling at the current price. This is the single-transaction case that
underpins many trading / time-series interview questions.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def max_profit(prices: list[int]) -> int:
    """Return the maximum profit from a single buy-then-sell transaction."""
    if not prices:
        return 0
    min_price = prices[0]
    best = 0
    for price in prices[1:]:
        best = max(best, price - min_price)
        min_price = min(min_price, price)
    return best


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    print("best_time_to_buy_and_sell_stock: OK")
