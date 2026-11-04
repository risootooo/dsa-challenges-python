"""
Problem: Group Anagrams
Group a list of strings so that anagrams are in the same group.
Example: ["eat","tea","tan","ate","nat","bat"]
         -> [["eat","tea","ate"], ["tan","nat"], ["bat"]] (any order)

Approach: Anagrams share the same sorted string. Use that sorted string
as a hash-map key and collect the originals under it.

Time Complexity: O(n * k log k) for n strings of max length k
Space Complexity: O(n * k)
"""

from __future__ import annotations

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group anagrams together; group order is not significant."""
    groups: dict[str, list[str]] = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    result = {frozenset(g) for g in group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])}
    assert result == {frozenset({"eat", "tea", "ate"}), frozenset({"tan", "nat"}), frozenset({"bat"})}
    print("group_anagrams: OK")
