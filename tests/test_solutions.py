"""Tests for the DSA solutions in this repository.

Modules are loaded directly from their file paths so the tests run
regardless of package/import configuration:

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


# --- Arrays ---------------------------------------------------------------

def test_max_subarray():
    mod = load("arrays/max_subarray.py")
    assert mod.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert mod.max_subarray([1]) == 1
    assert mod.max_subarray([5, 4, -1, 7, 8]) == 23
    assert mod.max_subarray([-1, -2]) == -1


def test_product_except_self():
    mod = load("arrays/product_except_self.py")
    assert mod.product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert mod.product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_rotate_array():
    mod = load("arrays/rotate_array.py")
    data = [1, 2, 3, 4, 5, 6, 7]
    mod.rotate(data, 3)
    assert data == [5, 6, 7, 1, 2, 3, 4]
    data2 = [-1, -100, 3, 99]
    mod.rotate(data2, 2)
    assert data2 == [3, 99, -1, -100]


def test_best_time_to_buy_and_sell_stock():
    mod = load("arrays/best_time_to_buy_and_sell_stock.py")
    assert mod.max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert mod.max_profit([7, 6, 4, 3, 1]) == 0
    assert mod.max_profit([]) == 0


# --- Strings ---------------------------------------------------------------

def test_valid_anagram():
    mod = load("strings/valid_anagram.py")
    assert mod.is_anagram("anagram", "nagaram") is True
    assert mod.is_anagram("rat", "car") is False
    assert mod.is_anagram("", "") is True


def test_longest_common_prefix():
    mod = load("strings/longest_common_prefix.py")
    assert mod.longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert mod.longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert mod.longest_common_prefix([]) == ""


def test_reverse_words():
    mod = load("strings/reverse_words_in_a_string.py")
    assert mod.reverse_words("the sky is blue") == "blue is sky the"
    assert mod.reverse_words("  hello world  ") == "world hello"
    assert mod.reverse_words("a good   example") == "example good a"


# --- Hash maps -------------------------------------------------------------

def test_two_sum():
    mod = load("hashmaps/two_sum.py")
    assert mod.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert mod.two_sum([3, 2, 4], 6) == [1, 2]
    assert mod.two_sum([3, 3], 6) == [0, 1]


def test_group_anagrams():
    mod = load("hashmaps/group_anagrams.py")
    result = {frozenset(g) for g in mod.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])}
    assert result == {
        frozenset({"eat", "tea", "ate"}),
        frozenset({"tan", "nat"}),
        frozenset({"bat"}),
    }
    assert mod.group_anagrams([]) == []


# --- Two pointers ----------------------------------------------------------

def test_valid_palindrome():
    mod = load("two_pointers/valid_palindrome.py")
    assert mod.is_palindrome("A man, a plan, a canal: Panama") is True
    assert mod.is_palindrome("race a car") is False
    assert mod.is_palindrome(" ") is True


def test_container_with_most_water():
    mod = load("two_pointers/container_with_most_water.py")
    assert mod.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert mod.max_area([1, 1]) == 1


def test_three_sum():
    mod = load("two_pointers/three_sum.py")
    assert mod.three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert mod.three_sum([0, 1, 1]) == []
    assert mod.three_sum([0, 0, 0]) == [[0, 0, 0]]


# --- Sliding window --------------------------------------------------------

def test_longest_substring_without_repeating():
    mod = load("sliding_window/longest_substring_without_repeating.py")
    assert mod.length_of_longest_substring("abcabcbb") == 3
    assert mod.length_of_longest_substring("bbbbb") == 1
    assert mod.length_of_longest_substring("pwwkew") == 3
    assert mod.length_of_longest_substring("") == 0


def test_minimum_window_substring():
    mod = load("sliding_window/minimum_window_substring.py")
    assert mod.min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert mod.min_window("a", "a") == "a"
    assert mod.min_window("a", "aa") == ""


# --- Binary search ---------------------------------------------------------

def test_binary_search():
    mod = load("binary_search/binary_search.py")
    assert mod.binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert mod.binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert mod.binary_search([5], 5) == 0


def test_search_in_rotated_sorted_array():
    mod = load("binary_search/search_in_rotated_sorted_array.py")
    assert mod.search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert mod.search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert mod.search_rotated([1], 0) == -1


# --- Stack -----------------------------------------------------------------

def test_valid_parentheses():
    mod = load("stack/valid_parentheses.py")
    assert mod.is_valid_parentheses("()") is True
    assert mod.is_valid_parentheses("()[]{}") is True
    assert mod.is_valid_parentheses("(]") is False
    assert mod.is_valid_parentheses("([{}])") is True


def test_daily_temperatures():
    mod = load("stack/daily_temperatures.py")
    assert mod.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert mod.daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]


# --- Linked list -----------------------------------------------------------

def test_reverse_linked_list():
    mod = load("linked_list/reverse_linked_list.py")
    assert mod.list_to_array(mod.reverse_list(mod.build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert mod.list_to_array(mod.reverse_list(mod.build_list([]))) == []
    assert mod.list_to_array(mod.reverse_list(mod.build_list([1]))) == [1]


def test_merge_two_sorted_lists():
    mod = load("linked_list/merge_two_sorted_lists.py")
    merged = mod.merge_two_lists(mod.build_list([1, 2, 4]), mod.build_list([1, 3, 4]))
    assert mod.list_to_array(merged) == [1, 1, 2, 3, 4, 4]
    assert mod.list_to_array(mod.merge_two_lists(mod.build_list([]), mod.build_list([0]))) == [0]


# --- Trees -----------------------------------------------------------------

def _sample_tree(mod):
    return mod.TreeNode(3, mod.TreeNode(9), mod.TreeNode(20, mod.TreeNode(15), mod.TreeNode(7)))


def test_maximum_depth_of_binary_tree():
    mod = load("trees/maximum_depth_of_binary_tree.py")
    tree = _sample_tree(mod)
    assert mod.max_depth(tree) == 3
    assert mod.max_depth_bfs(tree) == 3
    assert mod.max_depth(None) == 0


def test_invert_binary_tree():
    mod = load("trees/invert_binary_tree.py")
    tree = mod.TreeNode(4, mod.TreeNode(2, mod.TreeNode(1), mod.TreeNode(3)),
                           mod.TreeNode(7, mod.TreeNode(6), mod.TreeNode(9)))
    inverted = mod.invert_tree(tree)
    assert inverted.left.val == 7 and inverted.right.val == 2
    assert inverted.left.left.val == 9 and inverted.right.right.val == 1
    assert mod.invert_tree(None) is None


def test_binary_tree_level_order_traversal():
    mod = load("trees/binary_tree_level_order_traversal.py")
    tree = _sample_tree(mod)
    assert mod.level_order(tree) == [[3], [9, 20], [15, 7]]
    assert mod.level_order(None) == []


# --- Graphs ----------------------------------------------------------------

def test_number_of_islands():
    mod = load("graphs/number_of_islands.py")
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert mod.num_islands(grid) == 3
    assert mod.num_islands([["0", "0"], ["0", "0"]]) == 0
    # Input must not be mutated
    assert grid[0][0] == "1"


def test_flood_fill():
    mod = load("graphs/flood_fill.py")
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    assert mod.flood_fill(image, 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert image == [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def test_clone_graph():
    mod = load("graphs/clone_graph.py")
    assert mod.clone_graph(None) is None
    n1, n2, n3, n4 = mod.Node(1), mod.Node(2), mod.Node(3), mod.Node(4)
    n1.neighbors, n2.neighbors = [n2, n4], [n1, n3]
    n3.neighbors, n4.neighbors = [n2, n4], [n1, n3]
    copy_root = mod.clone_graph(n1)
    # Same structure, brand-new objects
    assert copy_root is not n1 and copy_root.val == 1
    assert sorted(n.val for n in copy_root.neighbors) == [2, 4]
    copied_two = next(n for n in copy_root.neighbors if n.val == 2)
    assert copied_two is not n2
    assert sorted(n.val for n in copied_two.neighbors) == [1, 3]
    # Deep copy: mutating the clone leaves the original untouched
    copied_two.val = 99
    assert n2.val == 2


# --- Heap ------------------------------------------------------------------

def test_kth_largest_element():
    mod = load("heap/kth_largest_element.py")
    assert mod.find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert mod.find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_top_k_frequent_elements():
    mod = load("heap/top_k_frequent_elements.py")
    assert set(mod.top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert mod.top_k_frequent([1], 1) == [1]


# --- Dynamic programming ---------------------------------------------------

def test_climbing_stairs():
    mod = load("dynamic_programming/climbing_stairs.py")
    assert mod.climb_stairs(2) == 2
    assert mod.climb_stairs(3) == 3
    assert mod.climb_stairs(5) == 8


def test_coin_change():
    mod = load("dynamic_programming/coin_change.py")
    assert mod.coin_change([1, 2, 5], 11) == 3
    assert mod.coin_change([2], 3) == -1
    assert mod.coin_change([1], 0) == 0


def test_house_robber():
    mod = load("dynamic_programming/house_robber.py")
    assert mod.rob([1, 2, 3, 1]) == 4
    assert mod.rob([2, 7, 9, 3, 1]) == 12
    assert mod.rob([]) == 0


def test_longest_common_subsequence():
    mod = load("dynamic_programming/longest_common_subsequence.py")
    assert mod.longest_common_subsequence("abcde", "ace") == 3
    assert mod.longest_common_subsequence("abc", "def") == 0
    assert mod.longest_common_subsequence("abc", "abc") == 3
    assert mod.longest_common_subsequence("", "abc") == 0
    assert mod.longest_common_subsequence("AGGTAB", "GXTXAYB") == 4
    # Reconstruction returns a real common subsequence of optimal length
    sub = mod.lcs_string("abcde", "ace")
    assert sub == "ace"
    sub2 = mod.lcs_string("AGGTAB", "GXTXAYB")
    assert len(sub2) == 4
    it = iter("AGGTAB")
    assert all(ch in it for ch in sub2)  # subsequence of text1, in order
