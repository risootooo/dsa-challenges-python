"""
Problem: Reverse Words in a String
Reverse the order of words in a string, collapsing extra spaces.
Example: "  the sky is blue  " -> "blue is sky the"

Approach: Split on whitespace (which normalises spacing), reverse the
word list, and join with single spaces.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def reverse_words(s: str) -> str:
    """Return ``s`` with its words in reverse order, single-spaced."""
    return " ".join(reversed(s.split()))


if __name__ == "__main__":
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello world  ") == "world hello"
    print("reverse_words_in_a_string: OK")
