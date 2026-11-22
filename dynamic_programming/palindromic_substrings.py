"""
Problem: Palindromic Substrings
Given a string, count how many of its substrings are palindromes.
Substrings at different positions count separately even when their
text is identical.
Example: "abc" -> 3 ("a", "b", "c"); "aaa" -> 6 ("a" x3, "aa" x2,
"aaa"); "abba" -> 6 ("a", "b", "b", "a", "bb", "abba")

Approach: Expand around every possible centre. Each index is the
centre of an odd-length palindrome and each adjacent pair is the
centre of an even-length palindrome. Expanding outwards while the
ends match counts one palindrome per successful step, so every
palindromic substring is counted exactly once, by its centre.

Time Complexity: O(n^2)
Space Complexity: O(1) extra
"""

from __future__ import annotations


def count_substrings(s: str) -> int:
    """Number of palindromic substrings of ``s``."""
    if not s:
        return 0
    count = 0

    def expand(left: int, right: int) -> int:
        found = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            found += 1
            left -= 1
            right += 1
        return found

    for centre in range(len(s)):
        count += expand(centre, centre)
        count += expand(centre, centre + 1)
    return count


if __name__ == "__main__":
    assert count_substrings("abc") == 3
    assert count_substrings("aaa") == 6
    assert count_substrings("abba") == 6
    assert count_substrings("") == 0
    assert count_substrings("a") == 1
    assert count_substrings("ab") == 2
    assert count_substrings("aa") == 3
    assert count_substrings("racecar") == 10
    print("palindromic_substrings: OK")
