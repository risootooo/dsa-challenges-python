# DSA Challenges — Python

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Tests](https://img.shields.io/badge/tests-62%20passing-brightgreen.svg)
![Problems](https://img.shields.io/badge/problems-62-orange.svg)
![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg)

A practice and portfolio repository of **62 data structures and algorithms
problems solved in clean, typed Python 3**, organised by topic — from
foundations (arrays, hash maps, two pointers) through an **advanced tier**:
system-design data structures (LRU cache), tries, weighted graph algorithms
(Dijkstra, Bellman-Ford, Union-Find, topological sort), two-heap medians,
and advanced dynamic programming.

Each solution is a runnable module — not a platform snippet — with a
docstring stating the problem, the approach, and its time/space
complexity, plus a `__main__` self-check. A pytest suite covers all 62
solutions, and the companion docs distil the reusable patterns:

- 📖 **[Pattern Playbook](docs/PATTERNS.md)** — templates for two pointers,
  sliding window, BFS/DFS, binary search on the answer, DP states,
  Dijkstra, Union-Find, tries, monotonic stacks and heaps, with
  when-to-use guidance.
- 📊 **[Complexity Cheat Sheet](docs/COMPLEXITY.md)** — Big-O tables for the
  core structures and every algorithm in the repo.

> This is a personal practice / portfolio repository built for interview
> preparation and skill development. It is not a record of submissions on
> any coding platform.

## About

I'm Samrat Banerjee — a BCA (Hons) graduate with a finance focus
(equity research, quantitative projects, and an MBA in Financial
Management in progress). This repository is the algorithms side of that
profile: the patterns below — two pointers, sliding window, binary
search, heaps, dynamic programming, graph algorithms — are the same
patterns that show up in screening rounds for analyst, research, and
finance-tech roles.

## Problems — Foundations (1–30)

| # | Problem | Topic | Difficulty | Time | Space |
|---|---------|-------|------------|------|-------|
| 1 | Maximum Subarray | Arrays | Medium | O(n) | O(1) |
| 2 | Product of Array Except Self | Arrays | Medium | O(n) | O(1) extra |
| 3 | Rotate Array | Arrays | Medium | O(n) | O(1) |
| 4 | Best Time to Buy and Sell Stock | Arrays | Easy | O(n) | O(1) |
| 5 | Valid Anagram | Strings | Easy | O(n) | O(k) |
| 6 | Longest Common Prefix | Strings | Easy | O(n·m) | O(1) extra |
| 7 | Reverse Words in a String | Strings | Medium | O(n) | O(n) |
| 8 | Two Sum | Hash Maps | Easy | O(n) | O(n) |
| 9 | Group Anagrams | Hash Maps | Medium | O(n·k log k) | O(n·k) |
| 10 | Valid Palindrome | Two Pointers | Easy | O(n) | O(1) |
| 11 | Container With Most Water | Two Pointers | Medium | O(n) | O(1) |
| 12 | 3Sum | Two Pointers | Medium | O(n²) | O(1) extra |
| 13 | Longest Substring Without Repeating Characters | Sliding Window | Medium | O(n) | O(min(n, Σ)) |
| 14 | Minimum Window Substring | Sliding Window | Hard | O(\|s\|+\|t\|) | O(\|t\|) |
| 15 | Binary Search | Binary Search | Easy | O(log n) | O(1) |
| 16 | Search in Rotated Sorted Array | Binary Search | Medium | O(log n) | O(1) |
| 17 | Valid Parentheses | Stack | Easy | O(n) | O(n) |
| 18 | Daily Temperatures | Stack | Medium | O(n) | O(n) |
| 19 | Reverse Linked List | Linked List | Easy | O(n) | O(1) |
| 20 | Merge Two Sorted Lists | Linked List | Easy | O(n+m) | O(1) extra |
| 21 | Maximum Depth of Binary Tree | Trees | Easy | O(n) | O(h) |
| 22 | Invert Binary Tree | Trees | Easy | O(n) | O(h) |
| 23 | Binary Tree Level Order Traversal | Trees | Medium | O(n) | O(n) |
| 24 | Number of Islands | Graphs | Medium | O(rows·cols) | O(rows·cols) |
| 25 | Flood Fill | Graphs | Easy | O(rows·cols) | O(rows·cols) |
| 26 | Kth Largest Element in an Array | Heap | Medium | O(n log k) | O(k) |
| 27 | Top K Frequent Elements | Heap / Bucket | Medium | O(n) | O(n) |
| 28 | Climbing Stairs | Dynamic Programming | Easy | O(n) | O(1) |
| 29 | Coin Change | Dynamic Programming | Medium | O(amount·coins) | O(amount) |
| 30 | House Robber | Dynamic Programming | Medium | O(n) | O(1) |

## Problems — Advanced (31–62)

The advanced tier targets the patterns that separate screening rounds from
final rounds: designing data structures under strict complexity budgets,
weighted graph algorithms, and DP where the state definition is the problem.

| # | Problem | Topic | Difficulty | Time | Space |
|---|---------|-------|------------|------|-------|
| 31 | LRU Cache | Design | Medium | O(1) get/put | O(capacity) |
| 32 | Min Stack | Design | Medium | O(1) all ops | O(n) |
| 33 | Implement Trie (Prefix Tree) | Tries | Medium | O(L) per op | O(total chars) |
| 34 | Word Search II | Tries | Hard | O(m·n·4^L) worst | O(total chars) |
| 35 | Dijkstra's Shortest Path | Advanced Graphs | Medium | O((V+E) log V) | O(V+E) |
| 36 | Network Delay Time | Advanced Graphs | Medium | O((V+E) log V) | O(V+E) |
| 37 | Course Schedule (Topological Sort) | Advanced Graphs | Medium | O(V+E) | O(V+E) |
| 38 | Redundant Connection (Union-Find) | Advanced Graphs | Medium | O(n·α(n)) | O(n) |
| 39 | Cheapest Flights Within K Stops (Bellman-Ford) | Advanced Graphs | Medium | O(k·E) | O(V) |
| 40 | Find Median from Data Stream (Two Heaps) | Heap | Hard | O(log n) add, O(1) median | O(n) |
| 41 | Merge K Sorted Lists | Heap | Hard | O(N log k) | O(k) |
| 42 | Sliding Window Maximum (Monotonic Deque) | Sliding Window | Hard | O(n) | O(k) |
| 43 | Longest Increasing Subsequence | Advanced DP | Medium | O(n log n) | O(n) |
| 44 | Edit Distance | Advanced DP | Medium | O(m·n) | O(n) |
| 45 | 0/1 Knapsack | Advanced DP | Medium | O(n·capacity) | O(capacity) |
| 46 | Word Break | Advanced DP | Medium | O(n·L) | O(n) |
| 47 | KMP Pattern Search | Strings | Hard | O(n+m) | O(m) |
| 48 | Longest Palindromic Substring | Strings | Medium | O(n²) | O(1) extra |
| 49 | Serialize and Deserialize Binary Tree | Trees | Hard | O(n) | O(n) |
| 50 | Binary Tree Maximum Path Sum | Trees | Hard | O(n) | O(h) |
| 51 | Clone Graph | Graphs | Medium | O(V+E) | O(V) |
| 52 | Longest Common Subsequence | Dynamic Programming | Medium | O(m·n) | O(min(m,n)) |
| 53 | Validate Binary Search Tree | Trees | Medium | O(n) | O(h) |
| 54 | Search a 2D Matrix | Binary Search | Medium | O(log(m·n)) | O(1) |
| 55 | Rotting Oranges | Graphs | Medium | O(rows·cols) | O(rows·cols) |
| 56 | Decode Ways | Dynamic Programming | Medium | O(n) | O(1) |
| 57 | Course Schedule II | Advanced Graphs | Medium | O(V+E) | O(V+E) |
| 58 | Binary Tree Right Side View | Trees | Medium | O(n) | O(n) |
| 59 | Pacific Atlantic Water Flow | Graphs | Medium | O(rows·cols) | O(rows·cols) |
| 60 | Lowest Common Ancestor of a Binary Tree | Trees | Medium | O(n) | O(h) |
| 61 | Merge Intervals | Intervals | Medium | O(n log n) | O(n) |
| 62 | Combination Sum | Backtracking | Medium | O(N^(T/M)) | O(T/M) |

Difficulty is the commonly used Easy / Medium / Hard grading for these
well-known problem patterns.

## Repository structure

```
dsa-challenges-python/
├── arrays/               # Kadane's, prefix/suffix products, rotation, stock profit
├── strings/              # anagrams, prefixes, KMP search, palindromic substrings
├── hashmaps/             # two sum, grouping by canonical key
├── two_pointers/         # palindrome, container, 3Sum
├── sliding_window/       # longest/minimum window, monotonic-deque maximum
├── binary_search/        # classic, rotated array, 2D matrix
├── stack/                # parentheses, monotonic stack
├── linked_list/          # reversal, merging (with ListNode helpers)
├── trees/                # depth, inversion, BFS order, serialization, max path sum, BST validation, LCA
├── graphs/               # island counting, flood fill (grid DFS), rotting oranges (BFS), pacific-atlantic
├── heap/                 # kth largest, top-k, merge K lists, two-heap median
├── dynamic_programming/  # stairs, coin change, house robber, LCS, decode ways
├── design/               # LRU cache (hash map + doubly linked list), min stack
├── tries/                # trie implementation, word search II
├── advanced_graphs/      # Dijkstra, Bellman-Ford, Kahn topo sort, union-find
├── advanced_dp/          # LIS O(n log n), edit distance, knapsack, word break
├── intervals/            # merge intervals (sort + sweep)
├── backtracking/         # combination sum (DFS with pruning)
├── docs/
│   ├── PATTERNS.md       # reusable pattern templates + when to use each
│   └── COMPLEXITY.md     # Big-O cheat sheet for structures & algorithms here
└── tests/
    ├── test_solutions.py # pytest suite: problems 1–62 (foundations + later additions)
    └── test_advanced.py  # pytest suite: problems 31–50
```

## Run the tests

Requires Python 3.10+.

```bash
pip install -r requirements.txt
python -m pytest -q
```

Run any single solution directly, e.g.:

```bash
python arrays/max_subarray.py
python design/lru_cache.py
python advanced_graphs/dijkstra.py
```

## Learning roadmap

How this set was built, and a sensible order to study it in:

1. **Foundations** — Arrays, Strings, Hash Maps (Two Sum → Group Anagrams)
2. **Pointer patterns** — Two Pointers, then Sliding Window
3. **Log-time search** — Binary Search, including the rotated-array variant
4. **Linear structures** — Stack (incl. monotonic stack), Linked List
5. **Hierarchies & grids** — Trees (DFS + BFS), Graphs (grid DFS)
6. **Selection problems** — Heap / top-k patterns
7. **Optimisation** — Dynamic Programming (1-D DP first: stairs, robber, coins)
8. **Design** — LRU Cache and Min Stack: data structures under O(1) budgets
9. **String algorithms** — Trie, KMP, expand-around-centre palindromes
10. **Weighted graphs** — Dijkstra, Bellman-Ford, Union-Find, topological sort
11. **Advanced DP** — state design: LIS, edit distance, knapsack, word break

**Next steps I plan to add:** more backtracking
(subsets / permutations / N-Queens), more interval problems,
segment tree / BIT, and timed re-solves of the Hard problems above.

## Notes on style

- Type hints on every function; `from __future__ import annotations`.
- No platform-specific `Solution` class wrappers — plain functions and
  small classes that can be imported, tested, and reused.
- Linked-list and tree solutions include small node definitions and
  builder helpers so they run standalone.
- Advanced solutions state *why* the algorithm works (invariants, pruning,
  ordering tricks), not just what it does — see the knapsack descending-loop
  and bounded Bellman-Ford notes.

## License

MIT — see [LICENSE](LICENSE) if present, otherwise treat code in this
repository as available for learning and reference with attribution.
