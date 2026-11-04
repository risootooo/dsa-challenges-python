"""Tests for the advanced DSA solutions (problems 31-50).

Uses the same path-based module loading as test_solutions.py so the tests
run regardless of package/import configuration:

    python -m pytest -q
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]


def load(relative_path: str) -> ModuleType:
    """Load a solution module from its path relative to the repo root."""
    path = ROOT / relative_path
    name = path.stem
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# --- Design ----------------------------------------------------------------

def test_lru_cache():
    mod = load("design/lru_cache.py")
    cache = mod.LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    cache.put(3, 30)  # update in place refreshes recency
    cache.put(5, 5)  # evicts key 4, not key 3
    assert cache.get(4) == -1
    assert cache.get(3) == 30


def test_min_stack():
    mod = load("design/min_stack.py")
    stack = mod.MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.get_min() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.get_min() == -2
    stack.push(-2)  # duplicate minimum survives one pop
    stack.pop()
    assert stack.get_min() == -2


# --- Tries -----------------------------------------------------------------

def test_trie():
    mod = load("tries/implement_trie.py")
    trie = mod.Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.search("apples") is False
    assert trie.starts_with("banana") is False


def test_word_search_ii():
    mod = load("tries/word_search_ii.py")
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    result = mod.find_words([row[:] for row in board], ["oath", "pea", "eat", "rain"])
    assert sorted(result) == ["eat", "oath"]
    assert mod.find_words([["a"]], ["a", "b"]) == ["a"]
    assert mod.find_words([], ["a"]) == []


# --- Advanced graphs ---------------------------------------------------------

def test_dijkstra():
    mod = load("advanced_graphs/dijkstra.py")
    assert mod.shortest_paths(3, [[0, 1, 1], [1, 2, 1], [0, 2, 4]], 0) == [0, 1, 2]
    assert mod.shortest_paths(4, [[0, 1, 5]], 0) == [0, 5, -1, -1]
    edges = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5]]
    assert mod.shortest_paths(4, edges, 0) == [0, 3, 1, 4]


def test_network_delay_time():
    mod = load("advanced_graphs/network_delay_time.py")
    assert mod.network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert mod.network_delay_time([[1, 2, 1]], 2, 1) == 1
    assert mod.network_delay_time([[1, 2, 1]], 2, 2) == -1


def test_course_schedule():
    mod = load("advanced_graphs/course_schedule.py")
    assert mod.can_finish(2, [[1, 0]]) is True
    assert mod.can_finish(2, [[1, 0], [0, 1]]) is False
    assert mod.can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    assert mod.can_finish(3, []) is True


def test_redundant_connection():
    mod = load("advanced_graphs/redundant_connection.py")
    assert mod.find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert mod.find_redundant_connection(
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]


def test_cheapest_flights_within_k_stops():
    mod = load("advanced_graphs/cheapest_flights_within_k_stops.py")
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert mod.find_cheapest_price(4, flights, 0, 3, 1) == 700
    assert mod.find_cheapest_price(4, flights, 0, 3, 0) == -1  # needs >= 1 stop
    assert mod.find_cheapest_price(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200


# --- Heap (advanced) ---------------------------------------------------------

def test_median_finder():
    mod = load("heap/find_median_from_data_stream.py")
    finder = mod.MedianFinder()
    finder.add_num(5)
    assert finder.find_median() == 5.0
    finder.add_num(15)
    assert finder.find_median() == 10.0
    finder.add_num(1)
    assert finder.find_median() == 5.0
    finder.add_num(3)
    assert finder.find_median() == 4.0
    finder.add_num(8)
    assert finder.find_median() == 5.0


def test_merge_k_sorted_lists():
    mod = load("heap/merge_k_sorted_lists.py")
    lists = [mod.build_list([1, 4, 5]), mod.build_list([1, 3, 4]), mod.build_list([2, 6])]
    assert mod.list_to_array(mod.merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert mod.list_to_array(mod.merge_k_lists([])) == []
    assert mod.list_to_array(mod.merge_k_lists([mod.build_list([]), None])) == []


def test_sliding_window_maximum():
    mod = load("sliding_window/sliding_window_maximum.py")
    assert mod.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert mod.max_sliding_window([1], 1) == [1]
    assert mod.max_sliding_window([9, 8, 7, 6], 2) == [9, 8, 7]
    assert mod.max_sliding_window([1, 2, 3, 4], 4) == [4]


# --- Advanced DP -------------------------------------------------------------

def test_longest_increasing_subsequence():
    mod = load("advanced_dp/longest_increasing_subsequence.py")
    assert mod.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert mod.length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert mod.length_of_lis([7, 7, 7, 7, 7]) == 1
    assert mod.length_of_lis([]) == 0
    assert mod.length_of_lis_dp([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6


def test_edit_distance():
    mod = load("advanced_dp/edit_distance.py")
    assert mod.min_distance("horse", "ros") == 3
    assert mod.min_distance("intention", "execution") == 5
    assert mod.min_distance("", "abc") == 3
    assert mod.min_distance("abc", "") == 3
    assert mod.min_distance("same", "same") == 0


def test_knapsack_01():
    mod = load("advanced_dp/knapsack_01.py")
    assert mod.knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
    assert mod.knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
    assert mod.knapsack([], [], 10) == 0
    assert mod.knapsack([10], [100], 5) == 0
    # 0/1, not unbounded: one item of weight 2 must not be reusable
    assert mod.knapsack([2], [3], 6) == 3


def test_word_break():
    mod = load("advanced_dp/word_break.py")
    assert mod.word_break("leetcode", ["leet", "code"]) is True
    assert mod.word_break("applepenapple", ["apple", "pen"]) is True
    assert mod.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


# --- Strings (advanced) --------------------------------------------------------

def test_kmp_pattern_search():
    mod = load("strings/kmp_pattern_search.py")
    assert mod.compute_prefix_function("ababaca") == [0, 0, 1, 2, 3, 0, 1]
    assert mod.kmp_search("abxabcabcaby", "abcaby") == [6]
    assert mod.kmp_search("aaaaa", "aaa") == [0, 1, 2]  # overlapping matches
    assert mod.kmp_search("abc", "d") == []


def test_longest_palindromic_substring():
    mod = load("strings/longest_palindromic_substring.py")
    assert mod.longest_palindrome("babad") in ("bab", "aba")
    assert mod.longest_palindrome("cbbd") == "bb"
    assert mod.longest_palindrome("a") == "a"
    assert mod.longest_palindrome("") == ""
    assert mod.longest_palindrome("forgeeksskeegfor") == "geeksskeeg"


# --- Trees (advanced) ----------------------------------------------------------

def test_serialize_deserialize_binary_tree():
    mod = load("trees/serialize_deserialize_binary_tree.py")
    codec = mod.Codec()
    tree = mod.TreeNode(1, mod.TreeNode(2),
                        mod.TreeNode(3, mod.TreeNode(4), mod.TreeNode(5)))
    encoded = codec.serialize(tree)
    assert encoded == "1,2,3,null,null,4,5"
    decoded = codec.deserialize(encoded)
    assert codec.serialize(decoded) == encoded
    assert decoded.left.val == 2 and decoded.right.left.val == 4
    assert codec.serialize(None) == ""
    assert codec.deserialize("") is None


def test_binary_tree_maximum_path_sum():
    mod = load("trees/binary_tree_maximum_path_sum.py")
    assert mod.max_path_sum(mod.TreeNode(1, mod.TreeNode(2), mod.TreeNode(3))) == 6
    tree = mod.TreeNode(-10, mod.TreeNode(9),
                        mod.TreeNode(20, mod.TreeNode(15), mod.TreeNode(7)))
    assert mod.max_path_sum(tree) == 42
    assert mod.max_path_sum(mod.TreeNode(-3)) == -3
