"""
Problem: Minimum Window Substring
Given strings s and t, return the smallest substring of s that contains
every character of t (with multiplicities), or "" if none exists.
Example: s="ADOBECODEBANC", t="ABC" -> "BANC"

Approach: Expand a window with the right pointer until it covers t, then
shrink from the left while it stays valid, recording the best window.
Character counts track how many required characters are satisfied.

Time Complexity: O(|s| + |t|)
Space Complexity: O(|t|)
"""

from __future__ import annotations

from collections import Counter


def min_window(s: str, t: str) -> str:
    """Return the minimum window of ``s`` covering all characters of ``t``."""
    if not s or not t:
        return ""
    need = Counter(t)
    required = len(need)
    window: dict[str, int] = {}
    formed = 0
    left = 0
    best_len = float("inf")
    best_left = 0
    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1
        if char in need and window[char] == need[char]:
            formed += 1
        while formed == required:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_left = left
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
            left += 1
    return "" if best_len == float("inf") else s[best_left : best_left + best_len]  # type: ignore[operator]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    print("minimum_window_substring: OK")
