"""
Problem: Merge Two Sorted Lists
Merge two sorted singly linked lists into one sorted list.
Example: [1,2,4] and [1,3,4] -> [1,1,2,3,4,4]

Approach: Dummy head plus a tail pointer. Repeatedly attach the smaller
of the two current nodes, then attach whatever remains.

Time Complexity: O(n + m)
Space Complexity: O(1) extra (reuses existing nodes)
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next: ListNode | None = None


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """Merge two sorted linked lists and return the merged head."""
    dummy = ListNode(0)
    tail = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 is not None else list2
    return dummy.next


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_to_array(head: ListNode | None) -> list[int]:
    out: list[int] = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    merged = merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))
    assert list_to_array(merged) == [1, 1, 2, 3, 4, 4]
    print("merge_two_sorted_lists: OK")
