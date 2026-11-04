"""
Problem: Longest Palindromic Substring
Return the longest substring of s that reads the same forwards and
backwards. If several share the maximum length, return any one of them.
Example: "babad" -> "bab" (or "aba");  "cbbd" -> "bb"

Approach: Expand around the centre. Every palindrome has a centre — either
a character (odd length) or the gap between two characters (even length).
For each of the 2n-1 centres, expand outwards while both sides match and
track the best window. This avoids the O(n^2) memory of the DP table and
the O(n^3) check-every-substring brute force.

Time Complexity: O(n^2) worst case
Space Complexity: O(1) extra (excluding the returned substring)
"""

from __future__ import annotations


def longest_palindrome(s: str) -> str:
    """Return a longest palindromic substring of `s`."""
    if len(s) < 2:
        return s

    start, max_len = 0, 1

    def expand(left: int, right: int) -> tuple[int, int]:
        """Expand around a centre; return (start, length) of the palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1

    for centre in range(len(s)):
        for left, right in ((centre, centre), (centre, centre + 1)):
            cand_start, cand_len = expand(left, right)
            if cand_len > max_len:
                start, max_len = cand_start, cand_len
    return s[start : start + max_len]


if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("") == ""
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    print("longest_palindromic_substring: OK")
