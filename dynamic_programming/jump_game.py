"""
Problem: Jump Game
Given an array nums where nums[i] is the maximum jump length from
index i, return True if the last index can be reached starting from
index 0.
Example: [2,3,1,1,4] -> True; [3,2,1,0,4] -> False

Approach: Greedy scan tracking the furthest index reachable so far.
Walk left to right: if the current index is beyond the furthest
reachable index, the scan is stuck and the answer is False; otherwise
extend the furthest reach with i + nums[i]. Reaching the end of the
scan means the last index is reachable. One pass suffices because
only the maximum reach matters — any index at or below it is itself
reachable, so no choice made earlier can do better.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def can_jump(nums: list[int]) -> bool:
    """Return True if the last index of `nums` is reachable from index 0."""
    if not nums:
        return False
    furthest = 0
    for i, jump in enumerate(nums):
        if i > furthest:
            return False
        furthest = max(furthest, i + jump)
        if furthest >= len(nums) - 1:
            return True
    return True


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    # A zero in the middle is fine when a longer jump clears it
    assert can_jump([2, 0, 0]) is True
    assert can_jump([1, 0, 1]) is False
    # Edge cases: empty input, single element (already at the end)
    assert can_jump([]) is False
    assert can_jump([0]) is True
    assert can_jump([2]) is True
    print("jump_game: OK")
