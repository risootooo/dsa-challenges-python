"""
Problem: Valid Palindrome
Return True if a string is a palindrome, considering only alphanumeric
characters and ignoring case.
Example: "A man, a plan, a canal: Panama" -> True

Approach: Two pointers from both ends. Skip non-alphanumeric characters,
compare lower-cased characters, move inward.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def is_palindrome(s: str) -> bool:
    """Return True if ``s`` is a palindrome ignoring case/punctuation."""
    lo, hi = 0, len(s) - 1
    while lo < hi:
        while lo < hi and not s[lo].isalnum():
            lo += 1
        while lo < hi and not s[hi].isalnum():
            hi -= 1
        if s[lo].lower() != s[hi].lower():
            return False
        lo += 1
        hi -= 1
    return True


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    print("valid_palindrome: OK")
