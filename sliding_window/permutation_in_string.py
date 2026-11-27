"""
Problem: Permutation in String
Given strings s1 and s2, return True if s2 contains a permutation of s1
(that is, a substring of s2 that is an anagram of s1), and False otherwise.
Example: s1 = "ab", s2 = "eidbaooo" -> True ("ba" is a permutation of "ab")
         s1 = "ab", s2 = "eidboaoo" -> False

Approach: Sliding window of fixed length len(s1) over s2. Count the
characters s1 needs and keep the counts of the current window; a window
matches when every character count agrees. Slide one character at a time,
adding the character entering on the right and removing the one leaving
on the left, and track how many distinct characters currently match their
required count so each slide is O(1). An empty s1 is trivially contained;
an s1 longer than s2 can never be contained.

Time Complexity: O(n), where n is len(s2)
Space Complexity: O(k), where k is the number of distinct characters
"""

from __future__ import annotations

from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    """Return True when some substring of ``s2`` is a permutation of ``s1``."""
    if not s1:
        return True
    if len(s1) > len(s2):
        return False
    need = Counter(s1)
    window: Counter[str] = Counter()
    matched = 0

    def add(char: str) -> None:
        nonlocal matched
        if char not in need:
            return
        if window[char] == need[char]:
            matched -= 1
        window[char] += 1
        if window[char] == need[char]:
            matched += 1

    def remove(char: str) -> None:
        nonlocal matched
        if char not in need:
            return
        if window[char] == need[char]:
            matched -= 1
        window[char] -= 1
        if window[char] == need[char]:
            matched += 1

    for index, char in enumerate(s2):
        add(char)
        if index >= len(s1):
            remove(s2[index - len(s1)])
        if index >= len(s1) - 1 and matched == len(need):
            return True
    return False


if __name__ == "__main__":
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False
    assert check_inclusion("adc", "dcda") is True
    assert check_inclusion("hello", "ooolleoooleh") is False
    # Edge cases: empty pattern, single character, pattern longer than text
    assert check_inclusion("", "abc") is True
    assert check_inclusion("a", "a") is True
    assert check_inclusion("a", "b") is False
    assert check_inclusion("abc", "ab") is False
    assert check_inclusion("abc", "") is False
    print("permutation_in_string: OK")
