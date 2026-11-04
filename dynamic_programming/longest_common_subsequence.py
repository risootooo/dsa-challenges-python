"""
Problem: Longest Common Subsequence (LCS)
Given two strings, return the length of their longest common subsequence.
A subsequence keeps relative order but need not be contiguous.
Example: ("abcde", "ace") -> 3   ("abc", "def") -> 0

Approach: Classic 2D dynamic programming, compressed to two rows.
dp[i][j] = LCS length of a[:i] and b[:j]:
  chars match    -> dp[i-1][j-1] + 1
  chars differ   -> max(dp[i-1][j], dp[i][j-1])
Only the previous row is ever read, so two rows suffice for the length.
Reconstructing an actual subsequence needs the full table (or Hirschberg's
algorithm); ``lcs_string`` below keeps the table for clarity.

Time Complexity: O(len(a) * len(b))
Space Complexity: O(min(len(a), len(b))) for the length, O(len(a) * len(b))
                  for reconstruction
"""

from __future__ import annotations


def longest_common_subsequence(text1: str, text2: str) -> int:
    """Length of the longest common subsequence of ``text1`` and ``text2``."""
    # Keep the shorter string on the row axis to minimise memory.
    if len(text2) > len(text1):
        text1, text2 = text2, text1
    previous = [0] * (len(text2) + 1)
    for ch1 in text1:
        current = [0] * (len(text2) + 1)
        for j, ch2 in enumerate(text2, start=1):
            if ch1 == ch2:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(previous[j], current[j - 1])
        previous = current
    return previous[-1]


def lcs_string(text1: str, text2: str) -> str:
    """One longest common subsequence, rebuilt from the full DP table."""
    m, n = len(text1), len(text2)
    table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    chars: list[str] = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            chars.append(text1[i - 1])
            i, j = i - 1, j - 1
        elif table[i - 1][j] >= table[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(chars))


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("abc", "abc") == 3
    assert lcs_string("abcde", "ace") == "ace"
    assert len(lcs_string("AGGTAB", "GXTXAYB")) == 4  # classic textbook pair
    print("longest_common_subsequence: OK")
