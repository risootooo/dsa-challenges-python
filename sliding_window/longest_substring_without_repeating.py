"""
Problem: Longest Substring Without Repeating Characters
Find the length of the longest substring with no repeated character.
Example: "abcabcbb" -> 3 ("abc")

Approach: Sliding window with a map from character to its last index.
When a character repeats inside the window, jump the left edge just past
its previous occurrence.

Time Complexity: O(n)
Space Complexity: O(min(n, alphabet size))
"""

from __future__ import annotations


def length_of_longest_substring(s: str) -> int:
    """Return the length of the longest repeat-free substring."""
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    print("longest_substring_without_repeating: OK")
