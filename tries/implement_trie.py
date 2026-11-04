"""
Problem: Implement Trie (Prefix Tree)
Implement a trie supporting insert(word), search(word) — exact match — and
starts_with(prefix).
Example: insert("apple"); search("apple") -> True; search("app") -> False;
         starts_with("app") -> True

Approach: Each node holds a dict of children keyed by character and an
end-of-word flag. Insert/search/prefix all walk (or create) one node per
character, so every operation is proportional to the word length and
independent of how many words the trie stores.

Time Complexity: O(L) per operation, L = word/prefix length
Space Complexity: O(total characters inserted) worst case
"""

from __future__ import annotations


class _TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, _TrieNode] = {}
        self.is_end = False


class Trie:
    """Prefix tree for exact and prefix string lookups."""

    def __init__(self) -> None:
        self.root = _TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, _TrieNode())
        node.is_end = True

    def _walk(self, text: str) -> _TrieNode | None:
        node = self.root
        for ch in text:
            nxt = node.children.get(ch)
            if nxt is None:
                return None
            node = nxt
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("apples") is False
    print("implement_trie: OK")
