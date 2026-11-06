"""
Problem: Course Schedule II
There are num_courses courses labelled 0..num_courses-1. prerequisites[i] =
[a, b] means course b must be taken before course a. Return an ordering of
the courses that respects every prerequisite, or an empty list if no such
ordering exists (the prerequisite graph contains a cycle).
Example: num_courses=2, prerequisites=[[1,0]] -> [0,1]
         num_courses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]] -> [0,2,1,3]

Approach: Kahn's algorithm (BFS topological sort), extending Course
Schedule: compute the in-degree of every course, queue all zero-in-degree
courses, and repeatedly remove one — appending it to the ordering and
decrementing its dependents' in-degrees, queueing any that reach zero.
The ordering is valid iff it contains all num_courses courses; a shorter
ordering means the remaining courses sit on a dependency cycle, so an
empty list is returned instead of a partial order.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from __future__ import annotations

from collections import deque


def find_order(
    num_courses: int, prerequisites: list[list[int]]
) -> list[int]:
    """Return a valid course ordering, or [] if a cycle makes it impossible."""
    if num_courses <= 0:
        return []
    adjacency: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        adjacency[prereq].append(course)
        indegree[course] += 1

    queue: deque[int] = deque(
        c for c in range(num_courses) if indegree[c] == 0
    )
    order: list[int] = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for dependent in adjacency[course]:
            indegree[dependent] -= 1
            if indegree[dependent] == 0:
                queue.append(dependent)
    return order if len(order) == num_courses else []


if __name__ == "__main__":
    assert find_order(2, [[1, 0]]) == [0, 1]
    assert find_order(2, [[1, 0], [0, 1]]) == []
    assert find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in (
        [0, 1, 2, 3],
        [0, 2, 1, 3],
    )
    assert find_order(1, []) == [0]
    assert find_order(3, []) == [0, 1, 2]
    assert find_order(0, []) == []
    print("course_schedule_ii: OK")
