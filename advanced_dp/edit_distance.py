"""
Problem: Edit Distance (Levenshtein)
Return the minimum number of single-character insertions, deletions and
replacements needed to turn word1 into word2.
Example: ("horse", "ros") -> 3;  ("intention", "execution") -> 5

Approach: DP over prefixes. dp[j] after processing i characters of word1 is
the edit distance between word1[:i] and word2[:j]. For each cell: deleting
from word1 costs dp_prev[j] + 1, inserting costs dp[j-1] + 1, and matching or
replacing the current characters costs dp_prev[j-1] (0 if equal, else 1).
Keeping only the previous row reduces memory from O(mn) to O(n).

Time Complexity: O(m * n)
Space Complexity: O(n)
"""

from __future__ import annotations


def min_distance(word1: str, word2: str) -> int:
    """Return the Levenshtein edit distance between word1 and word2."""
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))  # distance from "" to each prefix of word2
    for i in range(1, m + 1):
        current = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                current[j] = prev[j - 1]
            else:
                current[j] = 1 + min(
                    prev[j],      # delete word1[i-1]
                    current[j - 1],  # insert word2[j-1]
                    prev[j - 1],  # replace word1[i-1] with word2[j-1]
                )
        prev = current
    return prev[n]


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "abc") == 3
    assert min_distance("same", "same") == 0
    print("edit_distance: OK")
