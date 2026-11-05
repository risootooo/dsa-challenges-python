"""
Problem: Decode Ways
A message of digits maps letters 'A'..'Z' to "1".."26". Given a digit
string, count how many ways it can be decoded. A lone '0' and pairs
outside 10..26 are invalid, so strings containing them in forced
positions have 0 decodings.
Example: "12" -> 2 ("AB", "L"); "226" -> 3 ("BZ", "VF", "BBF");
"06" -> 0

Approach: One-dimensional DP scanned left to right with two rolling
variables. Let ways(i) be the decodings of the prefix ending at i.
A single digit extends the previous prefix only if it is not '0'; a
two-digit pair extends the prefix before it only if it lies in
10..26 (which also excludes leading-zero pairs). Only the last two
values are ever read, so the table compresses to O(1) space.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from __future__ import annotations


def num_decodings(s: str) -> int:
    """Number of ways to decode digit string ``s`` into letters."""
    if not s or s[0] == "0":
        return 0
    if any(not ch.isdigit() for ch in s):
        return 0
    # prev2 = ways for prefix before previous char, prev1 = ways up to it.
    prev2, prev1 = 1, 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != "0":
            current += prev1
        pair = int(s[i - 1 : i + 1])
        if 10 <= pair <= 26:
            current += prev2
        prev2, prev1 = prev1, current
    return prev1


if __name__ == "__main__":
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("06") == 0
    assert num_decodings("0") == 0
    assert num_decodings("") == 0
    assert num_decodings("1") == 1
    assert num_decodings("10") == 1
    assert num_decodings("27") == 1
    assert num_decodings("100") == 0
    assert num_decodings("11106") == 2
    print("decode_ways: OK")
