# DSA Challenges — Python

A practice and portfolio repository of **30 data structures and algorithms
problems solved in clean, typed Python 3**, organised by topic.

Each solution is a runnable module — not a platform snippet — with a
docstring stating the problem, the approach, and its time/space
complexity, plus a small `__main__` demo. A pytest suite covers all 30
solutions.

> This is a personal practice / portfolio repository built for interview
> preparation and skill development. It is not a record of submissions on
> any coding platform.

## About

I'm Samrat Banerjee — a BCA (Hons) graduate with a finance focus
(equity research, quantitative projects, and an MBA in Financial
Management in progress). This repository is the algorithms side of that
profile: the patterns below — two pointers, sliding window, binary
search, heaps, dynamic programming — are the same patterns that show up
in screening rounds for analyst, research, and finance-tech roles.

## Problems

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

Difficulty is the commonly used Easy / Medium / Hard grading for these
well-known problem patterns.

## Repository structure

```
dsa-challenges-python/
├── arrays/               # Kadane's, prefix/suffix products, rotation, stock profit
├── strings/              # anagrams, prefixes, word manipulation
├── hashmaps/             # two sum, grouping by canonical key
├── two_pointers/         # palindrome, container, 3Sum
├── sliding_window/       # longest substring, minimum window
├── binary_search/        # classic + rotated array
├── stack/                # parentheses, monotonic stack
├── linked_list/          # reversal, merging (with ListNode helpers)
├── trees/                # depth, inversion, BFS level order (with TreeNode)
├── graphs/               # island counting, flood fill (grid DFS)
├── heap/                 # kth largest, top-k frequent
├── dynamic_programming/  # stairs, coin change, house robber
└── tests/
    └── test_solutions.py # pytest suite covering all 30 solutions
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
python dynamic_programming/coin_change.py
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

**Next steps I plan to add:** interval problems, backtracking
(subsets / permutations), trie, and graph shortest paths (Dijkstra),
plus timed re-solves of the Medium/Hard problems above.

## Notes on style

- Type hints on every function; `from __future__ import annotations`.
- No platform-specific `Solution` class wrappers — plain functions that
  can be imported, tested, and reused.
- Linked-list and tree solutions include small node definitions and
  builder helpers so they run standalone.

## License

MIT — see [LICENSE](LICENSE) if present, otherwise treat code in this
repository as available for learning and reference with attribution.
