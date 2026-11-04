"""
Problem: KMP Pattern Search (Knuth-Morris-Pratt)
Find all starting indices at which a pattern occurs in a text, in linear
time, and expose the prefix function used to do it.
Example: text="abxabcabcaby", pattern="abcaby" -> [6]
         compute_prefix_function("ababaca") -> [0,0,1,2,3,0,1]

Approach: The prefix function pi[i] is the length of the longest proper
prefix of pattern[:i+1] that is also a suffix of it. During the scan, a
mismatch does not restart the comparison — the text pointer never moves
backwards; instead the matched length falls back to pi[matched-1], reusing
the overlap the prefix function already measured. This is what removes the
O(n*m) blow-up of naive search on inputs like "aaaaaab" / "aaab".

Time Complexity: O(n + m)
Space Complexity: O(m)
"""

from __future__ import annotations


def compute_prefix_function(pattern: str) -> list[int]:
    """Return pi where pi[i] = longest proper prefix of pattern[:i+1]
    that is also a suffix of pattern[:i+1]."""
    pi = [0] * len(pattern)
    length = 0  # length of the current candidate prefix
    for i in range(1, len(pattern)):
        while length > 0 and pattern[i] != pattern[length]:
            length = pi[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
        pi[i] = length
    return pi


def kmp_search(text: str, pattern: str) -> list[int]:
    """Return all start indices where `pattern` occurs in `text`."""
    if pattern == "":
        return list(range(len(text) + 1))
    pi = compute_prefix_function(pattern)
    matches: list[int] = []
    matched = 0  # length of the pattern prefix matched so far
    for i, ch in enumerate(text):
        while matched > 0 and ch != pattern[matched]:
            matched = pi[matched - 1]
        if ch == pattern[matched]:
            matched += 1
        if matched == len(pattern):
            matches.append(i - len(pattern) + 1)
            matched = pi[matched - 1]  # allow overlapping matches
    return matches


if __name__ == "__main__":
    assert compute_prefix_function("ababaca") == [0, 0, 1, 2, 3, 0, 1]
    assert kmp_search("abxabcabcaby", "abcaby") == [6]
    assert kmp_search("aaaaa", "aaa") == [0, 1, 2]
    assert kmp_search("hello", "ll") == [2]
    assert kmp_search("abc", "d") == []
    print("kmp_pattern_search: OK")
