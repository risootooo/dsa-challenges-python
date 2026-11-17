"""
Problem: Longest Repeating Character Replacement
Given a string s of uppercase English letters and an integer k, return
the length of the longest substring that can be turned into a run of a
single repeated character by replacing at most k characters inside it.
Example: "ABAB" with k=2 -> 4; "AABABBA" with k=1 -> 4

Approach: Sliding window. A window is feasible when its length minus
the count of its most frequent character is at most k, because exactly
those other characters need replacing. Grow the right edge one
character at a time, tracking per-character counts and the highest
count seen in the window; while the window is infeasible, shrink it
from the left. The best feasible window length seen is the answer.
A negative k is treated as no solution and returns -1; an empty
string returns 0.

Time Complexity: O(n)
Space Complexity: O(1) extra (at most 26 letter counts)
"""

from __future__ import annotations


def character_replacement(s: str, k: int) -> int:
    """Return the longest substring fixable with at most ``k`` swaps."""
    if k < 0:
        return -1
    if not s:
        return 0
    counts: dict[str, int] = {}
    left = 0
    best = 0
    max_count = 0
    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1
        max_count = max(max_count, counts[char])
        while (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
    assert character_replacement("ABCDE", 1) == 2
    assert character_replacement("BAAAB", 2) == 5
    # Edge cases: empty string, single character, no replacements needed
    assert character_replacement("", 3) == 0
    assert character_replacement("A", 0) == 1
    # No-solution sentinel: a negative budget can never be satisfied
    assert character_replacement("ABAB", -1) == -1
    print("longest_repeating_character_replacement: OK")
