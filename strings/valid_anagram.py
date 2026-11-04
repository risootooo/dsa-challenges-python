"""
Problem: Valid Anagram
Given two strings s and t, return True if t is an anagram of s.
Example: s="anagram", t="nagaram" -> True

Approach: Anagrams have identical character counts. Count characters with
a hash map (collections.Counter) and compare. Works for any alphabet,
unlike a fixed 26-slot array.

Time Complexity: O(n)
Space Complexity: O(k) where k is the number of distinct characters
"""

from __future__ import annotations

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """Return True if ``t`` is an anagram of ``s``."""
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    print("valid_anagram: OK")
