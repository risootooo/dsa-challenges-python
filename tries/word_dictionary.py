"""
Problem: Design Add and Search Words Data Structure (Word Dictionary)
Design a structure supporting add_word(word) and search(word), where
the search word may contain '.' characters that match any single
letter. A search matches only a stored word of the same length whose
letters agree at every non-'.' position.
Example: add_word("bad"); add_word("dad"); add_word("mad");
         search("pad") -> False; search(".ad") -> True;
         search("b..") -> True; search("b.") -> False

Approach: Store the words in a trie — each node holds a dict of
children keyed by character and an end-of-word flag, so add_word is
one walk creating at most one node per character. Search is a DFS
over the trie guided by the pattern: a letter follows the single
matching child, while a '.' branches over every child at that depth.
The search succeeds only when the pattern is exhausted exactly at a
node flagged end-of-word, which enforces both the length match and
that prefixes of stored words do not count as matches.

Time Complexity: O(L) for add_word; O(L) for search without dots,
O(26^d * L) worst case with d dots branching over the alphabet
Space Complexity: O(total characters inserted)
"""

from __future__ import annotations


class _TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.is_end = False


class WordDictionary:
    """Trie-backed dictionary whose search patterns may contain '.'."""

    def __init__(self) -> None:
        self.root = _TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._search_from(word, 0, self.root)

    def _search_from(self, word: str, index: int, node: _TrieNode) -> bool:
        if index == len(word):
            return node.is_end
        ch = word[index]
        if ch == ".":
            return any(
                self._search_from(word, index + 1, child)
                for child in node.children.values()
            )
        child = node.children.get(ch)
        return child is not None and self._search_from(word, index + 1, child)


if __name__ == "__main__":
    dictionary = WordDictionary()
    dictionary.add_word("bad")
    dictionary.add_word("dad")
    dictionary.add_word("mad")
    assert dictionary.search("pad") is False
    assert dictionary.search(".ad") is True
    assert dictionary.search("b..") is True
    assert dictionary.search("bad") is True
    # Length must match exactly: prefixes and extensions do not match
    assert dictionary.search("ba") is False
    assert dictionary.search("b.") is False
    assert dictionary.search("....") is False
    # A pattern of only dots matches any stored word of that length
    assert dictionary.search("...") is True
    # Edge cases: empty dictionary, empty pattern, re-adding a word
    empty = WordDictionary()
    assert empty.search("a") is False
    assert empty.search(".") is False
    assert empty.search("") is False
    dictionary.add_word("bad")
    assert dictionary.search("bad") is True
    print("word_dictionary: OK")
