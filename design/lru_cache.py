"""
Problem: LRU Cache
Design a cache with a fixed capacity that evicts the least recently used
entry when full. Both get(key) and put(key, value) must run in O(1).
Example: capacity 2; put(1,1), put(2,2), get(1) -> 1, put(3,3) evicts key 2,
         get(2) -> -1, put(4,4) evicts key 1, get(1) -> -1, get(3) -> 3

Approach: Hash map from key to node + doubly linked list ordered by recency
(most recent at the head). The map gives O(1) lookup; the list gives O(1)
move-to-front and O(1) eviction of the tail. Sentinel head/tail nodes remove
all edge-case branching when splicing nodes.

Time Complexity: O(1) average for get and put
Space Complexity: O(capacity)
"""

from __future__ import annotations


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    """Least-recently-used cache with O(1) get/put."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._map: dict[int, _Node] = {}
        self._head = _Node()  # sentinel: most recent side
        self._tail = _Node()  # sentinel: least recent side
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: _Node) -> None:
        assert node.prev is not None and node.next is not None
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: _Node) -> None:
        node.prev = self._head
        node.next = self._head.next
        assert self._head.next is not None
        self._head.next.prev = node
        self._head.next = node

    def get(self, key: int) -> int:
        node = self._map.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self._map.get(key)
        if node is not None:
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return
        node = _Node(key, value)
        self._map[key] = node
        self._add_to_front(node)
        if len(self._map) > self.capacity:
            lru = self._tail.prev
            assert lru is not None and lru is not self._head
            self._remove(lru)
            del self._map[lru.key]


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("lru_cache: OK")
