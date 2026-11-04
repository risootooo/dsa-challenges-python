"""
Problem: Longest Common Prefix
Find the longest prefix shared by every string in a list.
Example: ["flower", "flow", "flight"] -> "fl"

Approach: Take the first string as a candidate prefix and shrink it from
the right until every other string starts with it.

Time Complexity: O(n * m) where n is the number of strings, m prefix length
Space Complexity: O(1) extra
"""

from __future__ import annotations


def longest_common_prefix(strs: list[str]) -> str:
    """Return the longest common prefix, or "" if there is none."""
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    print("longest_common_prefix: OK")
