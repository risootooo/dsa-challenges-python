"""
Problem: Reverse Linked List
Reverse a singly linked list and return the new head.
Example: 1 -> 2 -> 3 -> 4 -> 5  becomes  5 -> 4 -> 3 -> 2 -> 1

Approach: Walk the list once with three pointers (previous, current,
next). Flip each node's next pointer to its predecessor as you go.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next: ListNode | None = None


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list iteratively and return its new head."""
    prev: ListNode | None = None
    current = head
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def build_list(values: list[int]) -> ListNode | None:
    """Helper: build a linked list from Python values (for tests/demos)."""
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_to_array(head: ListNode | None) -> list[int]:
    """Helper: flatten a linked list into a Python list."""
    out: list[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert list_to_array(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    print("reverse_linked_list: OK")
