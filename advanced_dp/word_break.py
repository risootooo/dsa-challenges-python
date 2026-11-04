"""
Problem: Word Break
Given a string s and a dictionary of words, return True if s can be
segmented into a space-separated sequence of dictionary words (words may be
reused).
Example: s="leetcode", dict=["leet","code"] -> True
         s="catsandog", dict=["cats","dog","sand","and","cat"] -> False

Approach: dp[i] is True iff the prefix s[:i] can be segmented. For each i,
try every split j < i: if dp[j] is True and s[j:i] is a dictionary word,
then dp[i] is True. A set makes word lookup O(1), and capping the inner scan
at the longest dictionary word length avoids wasted substring checks.

Time Complexity: O(n^2) worst case (O(n * L) with the length cap, L = longest word)
Space Complexity: O(n)
"""

from __future__ import annotations


def word_break(s: str, word_dict: list[str]) -> bool:
    """Return True iff `s` can be segmented into dictionary words."""
    words = set(word_dict)
    if not words:
        return s == ""
    max_len = max(len(w) for w in words)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"]) is True
    assert word_break("applepenapple", ["apple", "pen"]) is True
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    assert word_break("", ["a"]) is True
    print("word_break: OK")
