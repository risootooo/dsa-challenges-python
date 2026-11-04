"""
Problem: Course Schedule
There are num_courses courses labelled 0..num_courses-1. prerequisites[i] =
[a, b] means course b must be taken before course a. Return True if all
courses can be finished (the prerequisite graph is acyclic), else False.
Example: num_courses=2, prerequisites=[[1,0]] -> True
         num_courses=2, prerequisites=[[1,0],[0,1]] -> False

Approach: Kahn's algorithm (BFS topological sort). Compute the in-degree of
every course, queue all zero-in-degree courses, and repeatedly remove one —
decrementing its dependents' in-degrees and queueing any that reach zero.
Every course can be ordered iff all num_courses are processed; a leftover
means the remaining courses sit on a dependency cycle.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from __future__ import annotations

from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Return True iff the prerequisite graph has no cycle."""
    adjacency: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        adjacency[prereq].append(course)
        indegree[course] += 1

    queue: deque[int] = deque(c for c in range(num_courses) if indegree[c] == 0)
    taken = 0
    while queue:
        course = queue.popleft()
        taken += 1
        for dependent in adjacency[course]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)
    return taken == num_courses


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    assert can_finish(3, []) is True
    print("course_schedule: OK")
