"""
Problem: Merge K Sorted Lists
Merge k sorted linked lists into one sorted linked list and return its head.
Example: [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]

Approach: Min-heap of (value, list_index, node) holding the current head of
each non-empty list. Repeatedly pop the smallest head, append it to the
result, and push that list's next node. The list_index tie-breaker keeps
heap entries comparable when two lists share a value (nodes themselves are
not orderable). Each of the N nodes is pushed and popped exactly once.

Time Complexity: O(N log k), N = total nodes, k = number of lists
Space Complexity: O(k) for the heap (result list excluded)
"""

from __future__ import annotations

import heapq
from dataclasses import dataclass, field


@dataclass
class ListNode:
    val: int
    next: ListNode | None = field(default=None)


def build_list(values: list[int]) -> ListNode | None:
    """Build a linked list from values (test/demo helper)."""
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_to_array(head: ListNode | None) -> list[int]:
    """Flatten a linked list to a Python list (test/demo helper)."""
    values: list[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    """Merge k sorted linked lists into one sorted linked list."""
    heap: list[tuple[int, int, ListNode]] = []
    for index, head in enumerate(lists):
        if head is not None:
            heapq.heappush(heap, (head.val, index, head))

    dummy = ListNode(0)
    tail = dummy
    while heap:
        _, index, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, index, node.next))
    return dummy.next


if __name__ == "__main__":
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert list_to_array(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert list_to_array(merge_k_lists([])) == []
    assert list_to_array(merge_k_lists([build_list([])])) == []
    print("merge_k_sorted_lists: OK")
