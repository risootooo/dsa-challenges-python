"""
Problem: Find Median from Data Stream
Design a data structure that supports add_num(x) and find_median() for a
stream of numbers. For an even count the median is the mean of the two
middle values.
Example: add 5, 15, 1, 3 -> medians after each add: 5.0, 10.0, 5.0, 4.0

Approach: Two heaps split the stream in half. A max-heap `low` holds the
smaller half (simulated with negated values in Python's min-heap) and a
min-heap `high` holds the larger half. Invariants: every element of low is
<= every element of high, and len(low) is len(high) or len(high) + 1. The
median is then low's top, or the mean of both tops.

Time Complexity: O(log n) add, O(1) median
Space Complexity: O(n)
"""

from __future__ import annotations

import heapq


class MedianFinder:
    """Running median of a number stream, maintained with two heaps."""

    def __init__(self) -> None:
        self._low: list[int] = []   # max-heap via negation; smaller half
        self._high: list[int] = []  # min-heap; larger half

    def add_num(self, num: int) -> None:
        heapq.heappush(self._low, -num)
        # Keep all of low <= all of high: move low's max into high.
        heapq.heappush(self._high, -heapq.heappop(self._low))
        # Rebalance so low is the same size as high or one larger.
        if len(self._low) < len(self._high):
            heapq.heappush(self._low, -heapq.heappop(self._high))

    def find_median(self) -> float:
        if not self._low:
            raise ValueError("no numbers added yet")
        if len(self._low) > len(self._high):
            return float(-self._low[0])
        return (-self._low[0] + self._high[0]) / 2.0


if __name__ == "__main__":
    finder = MedianFinder()
    finder.add_num(5)
    assert finder.find_median() == 5.0
    finder.add_num(15)
    assert finder.find_median() == 10.0
    finder.add_num(1)
    assert finder.find_median() == 5.0
    finder.add_num(3)
    assert finder.find_median() == 4.0
    print("find_median_from_data_stream: OK")
