# Pattern Playbook

Most interview problems are variations on a small set of patterns. This
playbook gives the template for each pattern used in this repo, when to reach
for it, and the problems here that use it.

---

## 1. Two Pointers

**When:** sorted arrays, palindromes, pair sums, in-place compaction — any
problem where two ends (or a slow/fast pair) can converge on the answer.

```python
left, right = 0, len(nums) - 1
while left < right:
    if condition_met(nums[left], nums[right]):
        return answer
    elif need_larger():
        left += 1
    else:
        right -= 1
```

Used in: `two_pointers/` (Valid Palindrome, Container With Most Water,
3Sum), `arrays/rotate_array.py`.

## 2. Sliding Window

**When:** longest/shortest subarray or substring with a property that is
monotone as the window grows (at most K distinct, sum <= target, ...).
Maintain `[left, right)` and a frequency map; expand right, shrink left
while the window is invalid.

```python
from collections import Counter

count = Counter()
left = 0
for right, ch in enumerate(s):
    count[ch] += 1
    while window_invalid(count):
        count[s[left]] -= 1
        left += 1
    best = max(best, right - left + 1)
```

Used in: `sliding_window/` (Longest Substring Without Repeating, Minimum
Window Substring, Sliding Window Maximum — the deque variant for extrema).

## 3. BFS / DFS on Grids and Graphs

**When:** connectivity, islands, flood fill, shortest path in an
*unweighted* graph (BFS), reachability and traversal order (DFS).

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    seen = {start}
    while queue:
        node = queue.popleft()
        for nxt in neighbours(node):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
```

Used in: `graphs/` (Number of Islands, Flood Fill), `trees/` level order.

## 4. Binary Search on the Answer

**When:** "minimum X such that ..." / "maximum X such that ..." where
feasibility is monotone: if X works, every larger (or smaller) X works too.
Binary-search the answer space and test feasibility in O(n).

```python
lo, hi = low_bound, high_bound
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid          # mid works; try smaller
    else:
        lo = mid + 1      # mid impossible
return lo
```

Related: classic and rotated-array search in `binary_search/`, and the
`bisect_left` step inside the O(n log n) LIS in `advanced_dp/`.

## 5. Dynamic Programming — Defining the State

**When:** optimal substructure + overlapping subproblems. The craft is the
state definition; the transitions follow from it.

| Problem here | State | Transition idea |
|---|---|---|
| Climbing Stairs | `dp[i]` = ways to reach step i | `dp[i-1] + dp[i-2]` |
| Coin Change | `dp[a]` = min coins for amount a | try every coin as the last one |
| House Robber | `dp[i]` = best loot up to house i | skip or rob house i |
| Edit Distance | `dp[i][j]` = distance of prefixes | delete / insert / replace |
| 0/1 Knapsack | `dp[w]` = best value at capacity w | take or skip item — iterate w **descending** |
| LIS | `tails[l]` = smallest tail of a subsequence of length l+1 | `bisect_left` replace |
| Word Break | `dp[i]` = prefix `s[:i]` segmentable | split at a dictionary word |

Used in: `dynamic_programming/`, `advanced_dp/`.

## 6. Dijkstra (weighted shortest path)

**When:** shortest paths with **non-negative** weights. A priority queue of
(dist, node); skip stale entries; relax edges. Negative weights -> use
Bellman-Ford instead (see Cheapest Flights, where rounds are capped by the
stop limit).

```python
import heapq

dist[src] = 0
heap = [(0, src)]
while heap:
    d, u = heapq.heappop(heap)
    if d > dist[u]:
        continue  # stale
    for v, w in adj[u]:
        if d + w < dist[v]:
            dist[v] = d + w
            heapq.heappush(heap, (dist[v], v))
```

Used in: `advanced_graphs/dijkstra.py`, `advanced_graphs/network_delay_time.py`.

## 7. Union-Find (Disjoint Set Union)

**When:** dynamic connectivity, cycle detection in undirected graphs,
grouping (accounts, provinces, Kruskal's MST). Path compression + union by
rank make operations near-constant amortised.

```python
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):  # False means "already connected" -> cycle
    rx, ry = find(x), find(y)
    if rx == ry:
        return False
    parent[ry] = rx
    return True
```

Used in: `advanced_graphs/redundant_connection.py`.

## 8. Trie (Prefix Tree)

**When:** many prefix queries, autocomplete, dictionary word search on a
board, longest-common-prefix style problems. Insert/search/prefix are all
O(word length), independent of dictionary size.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def insert(root, word):
    node = root
    for ch in word:
        node = node.children.setdefault(ch, TrieNode())
    node.is_end = True
```

Used in: `tries/` (Implement Trie, Word Search II).

## 9. Monotonic Stack / Deque

**When:** next greater/smaller element, histogram problems, sliding-window
extrema. Keep candidates in monotone order; each element is pushed and
popped at most once, giving O(n) total.

Used in: `stack/daily_temperatures.py`,
`sliding_window/sliding_window_maximum.py`.

## 10. Heap / Priority Queue

**When:** top-K anything, merging sorted streams, running medians. Python's
`heapq` is a min-heap; negate values for a max-heap, and push a tie-breaker
index when values can tie and payloads are unorderable.

Used in: `heap/` (Kth Largest, Top K Frequent, Merge K Sorted Lists,
Find Median from Data Stream — the two-heap pattern).
