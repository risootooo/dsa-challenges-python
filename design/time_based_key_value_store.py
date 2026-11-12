"""
Problem: Time Based Key-Value Store
Design a key-value store where each key maps to values stamped with a
timestamp. set(key, value, timestamp) stores the value at that timestamp;
get(key, timestamp) returns the value set at the largest timestamp <= the
queried timestamp, or "" if none exists. Timestamps passed to set for a
given key are strictly increasing.
Example: set("foo", "bar", 1); get("foo", 1) -> "bar"; get("foo", 3) -> "bar";
         set("foo", "bar2", 4); get("foo", 4) -> "bar2"; get("foo", 5) -> "bar2"

Approach: Keep, per key, two parallel lists — timestamps (appended in
increasing order, so they stay sorted) and values. get binary-searches the
timestamp list with bisect_right for the insertion point just past the
query, then steps back one slot: that entry is the latest value at or
before the query. No entry (index -1) or an unknown key returns "".

Time Complexity: O(1) amortised for set, O(log n) for get, where n is the
                 number of versions stored for the key
Space Complexity: O(total number of set calls)
"""

from __future__ import annotations

from bisect import bisect_right


class TimeMap:
    """Time-based key-value store with binary-search lookups."""

    def __init__(self) -> None:
        self._times: dict[str, list[int]] = {}
        self._values: dict[str, list[str]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._times.setdefault(key, []).append(timestamp)
        self._values.setdefault(key, []).append(value)

    def get(self, key: str, timestamp: int) -> str:
        times = self._times.get(key)
        if not times:
            return ""
        idx = bisect_right(times, timestamp) - 1
        if idx < 0:
            return ""
        return self._values[key][idx]


if __name__ == "__main__":
    store = TimeMap()
    store.set("foo", "bar", 1)
    assert store.get("foo", 1) == "bar"
    assert store.get("foo", 3) == "bar"
    store.set("foo", "bar2", 4)
    assert store.get("foo", 4) == "bar2"
    assert store.get("foo", 5) == "bar2"
    assert store.get("foo", 0) == ""
    assert store.get("missing", 10) == ""
    print("time_based_key_value_store: OK")
