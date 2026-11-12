"""
Problem: Task Scheduler
Given tasks labelled by single letters and a cooling interval n, where the
same task must wait n slots between two executions, return the least number
of intervals needed to finish all tasks. The CPU may stay idle in a slot.
Example: tasks = ["A", "A", "A", "B", "B", "B"], n = 2 -> 8
         (A -> B -> idle -> A -> B -> idle -> A -> B)

Approach: Greedy simulation with a max-heap of remaining counts and a
cooldown queue. Each slot pops the most frequent remaining task, decrements
it, and — if work on it remains — parks it in the FIFO queue with the time
it becomes available again (now + n + 1). Tasks leaving the queue go back
on the heap. A slot with an empty heap is idle. Counting uses a max-heap
over negated counts because Python's heapq is a min-heap.

Time Complexity: O(T log k), where T is the total number of slots
                 (including idles) and k the number of distinct tasks
Space Complexity: O(k)
"""

from __future__ import annotations

import heapq
from collections import Counter, deque


def least_interval(tasks: list[str], n: int) -> int:
    """Return the minimum slots (tasks + idles) to run ``tasks``."""
    if not tasks:
        return 0
    if n == 0:
        return len(tasks)
    heap: list[int] = [-count for count in Counter(tasks).values()]
    heapq.heapify(heap)
    # Queue entries are (remaining count, time the task is available again).
    cooldown: deque[tuple[int, int]] = deque()
    time = 0
    while heap or cooldown:
        time += 1
        if heap:
            remaining = -heapq.heappop(heap) - 1
            if remaining > 0:
                cooldown.append((remaining, time + n))
        else:
            # Nothing runnable: jump straight to the next release time.
            time = cooldown[0][1]
        while cooldown and cooldown[0][1] == time:
            remaining, _ = cooldown.popleft()
            heapq.heappush(heap, -remaining)
    return time


if __name__ == "__main__":
    assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert least_interval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert least_interval([], 2) == 0
    assert least_interval(["A"], 5) == 1
    print("task_scheduler: OK")
