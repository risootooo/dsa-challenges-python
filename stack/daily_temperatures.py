"""
Problem: Daily Temperatures
For each day, return how many days until a warmer temperature, or 0.
Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]

Approach: Monotonic decreasing stack of day indices. When today's
temperature beats the day on top of the stack, that day's answer is the
distance between them; pop and repeat.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Return days to wait for a warmer temperature for each day."""
    result = [0] * len(temperatures)
    stack: list[int] = []  # indices, temperatures decreasing
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    print("daily_temperatures: OK")
