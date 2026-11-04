# Complexity Cheat Sheet

Big-O reference for the data structures and algorithms used in this repo.
n = input size, V = vertices, E = edges, k = window/heap parameter,
L = word length, h = tree height.

## Core data structures

| Structure | Access | Search | Insert | Delete | Notes |
|---|---|---|---|---|---|
| Array / list | O(1) | O(n) | O(1) amortised append, O(n) insert | O(n) | cache-friendly |
| Hash map / set | — | O(1) average, O(n) worst | O(1) average | O(1) average | worst case = hash collisions |
| Stack / queue (list/deque) | O(1) top/front | O(n) | O(1) | O(1) | deque gives O(1) at both ends |
| Doubly linked list | O(n) | O(n) | O(1) at a known node | O(1) at a known node | powers the LRU cache with a hash map |
| Binary heap | O(1) min/max peek | O(n) | O(log n) | O(log n) pop | heapify is O(n) |
| Binary search tree (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | unbalanced degrades to O(n) |
| Trie | — | O(L) | O(L) | O(L) | independent of dictionary size |
| Union-Find | — | O(alpha(n)) find | O(alpha(n)) union | — | alpha = inverse Ackermann, ~constant |

## Core algorithms in this repo

| Algorithm | Time | Space | Where |
|---|---|---|---|
| Binary search | O(log n) | O(1) | `binary_search/` |
| KMP string search | O(n + m) | O(m) | `strings/kmp_pattern_search.py` |
| BFS / DFS | O(V + E) | O(V) | `graphs/`, `trees/` |
| Topological sort (Kahn) | O(V + E) | O(V + E) | `advanced_graphs/course_schedule.py` |
| Dijkstra (binary heap) | O((V + E) log V) | O(V + E) | `advanced_graphs/` |
| Bellman-Ford (bounded rounds) | O(k * E) | O(V) | `advanced_graphs/cheapest_flights_within_k_stops.py` |
| Union-Find cycle detection | O(E * alpha(V)) | O(V) | `advanced_graphs/redundant_connection.py` |
| Kadane's (max subarray) | O(n) | O(1) | `arrays/max_subarray.py` |
| Sliding window | O(n) | O(k) or O(alphabet) | `sliding_window/` |
| Monotonic deque window max | O(n) | O(k) | `sliding_window/sliding_window_maximum.py` |
| Top-K via heap | O(n log k) | O(k) | `heap/` |
| Merge K sorted lists | O(N log k) | O(k) | `heap/merge_k_sorted_lists.py` |
| LIS (patience + bisect) | O(n log n) | O(n) | `advanced_dp/longest_increasing_subsequence.py` |
| Edit distance | O(m * n) | O(n) rolling rows | `advanced_dp/edit_distance.py` |
| 0/1 knapsack | O(n * capacity) | O(capacity) | `advanced_dp/knapsack_01.py` |
| Tree traversals | O(n) | O(h) recursion | `trees/` |
| LRU cache get/put | O(1) average | O(capacity) | `design/lru_cache.py` |

## Sorting reference

| Sort | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | yes |
| Quick sort | O(n log n) | O(n log n) | O(n^2) | O(log n) | no |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | no |
| TimSort (Python `sorted`) | O(n) | O(n log n) | O(n log n) | O(n) | yes |
| Counting / radix sort | O(n + k) | O(n + k) | O(n + k) | O(n + k) | yes |

## Rules of thumb

- O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)
- An extra hash map usually trades O(n) space for a factor-n time win.
- "At most K" constraints on subarrays/substrings usually mean sliding window.
- "K-th / top-K" usually means a heap of size K, not a full sort.
- Non-negative edge weights -> Dijkstra; negative weights -> Bellman-Ford;
  unweighted -> BFS.
- If the obvious DP is O(n^2), look for a monotone structure (bisect,
  monotonic stack, prefix sums) to shave a log factor or a dimension.
