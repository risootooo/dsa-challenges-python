"""
Problem: Min Stack
Design a stack supporting push, pop, top and retrieving the minimum element,
all in constant time.
Example: push(-2), push(0), push(-3) -> get_min() == -3; pop(); top() == 0;
         get_min() == -2

Approach: Keep a second stack of running minima alongside the main stack.
Every push appends min(value, current minimum); every pop removes from both
stacks, so the top of the auxiliary stack is always the minimum of everything
below it — even when the minimum itself is popped.

Time Complexity: O(1) for push, pop, top and get_min
Space Complexity: O(n)
"""

from __future__ import annotations


class MinStack:
    """Stack with O(1) access to its minimum element."""

    def __init__(self) -> None:
        self._stack: list[int] = []
        self._mins: list[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        self._mins.append(val if not self._mins else min(val, self._mins[-1]))

    def pop(self) -> None:
        if not self._stack:
            raise IndexError("pop from empty MinStack")
        self._stack.pop()
        self._mins.pop()

    def top(self) -> int:
        if not self._stack:
            raise IndexError("top of empty MinStack")
        return self._stack[-1]

    def get_min(self) -> int:
        if not self._mins:
            raise IndexError("get_min of empty MinStack")
        return self._mins[-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.get_min() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.get_min() == -2
    print("min_stack: OK")
