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


def test_validate_binary_search_tree():
    mod = load("trees/validate_binary_search_tree.py")
    assert mod.is_valid_bst(mod.TreeNode(2, mod.TreeNode(1), mod.TreeNode(3))) is True
    invalid = mod.TreeNode(5, mod.TreeNode(1), mod.TreeNode(4, mod.TreeNode(3), mod.TreeNode(6)))
    assert mod.is_valid_bst(invalid) is False
    # Equal values are not allowed on either side (strict ordering)
    assert mod.is_valid_bst(mod.TreeNode(2, mod.TreeNode(2))) is False
    assert mod.is_valid_bst(mod.TreeNode(2, None, mod.TreeNode(2))) is False
    # A node valid against its parent but violating an ancestor's bound
    tricky = mod.TreeNode(10, mod.TreeNode(5), mod.TreeNode(15, mod.TreeNode(6), mod.TreeNode(20)))
    assert mod.is_valid_bst(tricky) is False
    assert mod.is_valid_bst(None) is True
    assert mod.is_valid_bst(mod.TreeNode(1)) is True


def test_search_a_2d_matrix():
    mod = load("binary_search/search_a_2d_matrix.py")
    grid = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert mod.search_matrix(grid, 3) is True
    assert mod.search_matrix(grid, 13) is False
    assert mod.search_matrix(grid, 1) is True
    assert mod.search_matrix(grid, 60) is True
    assert mod.search_matrix(grid, 0) is False
    assert mod.search_matrix(grid, 61) is False
    assert mod.search_matrix([[1]], 1) is True
    assert mod.search_matrix([[1]], 2) is False
    assert mod.search_matrix([], 1) is False
    assert mod.search_matrix([[]], 1) is False


def test_rotting_oranges():
    mod = load("graphs/rotting_oranges.py")
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert mod.oranges_rotting(grid) == 4
    # Input must not be mutated
    assert grid == [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # A fresh orange walled off by empties can never rot
    assert mod.oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert mod.oranges_rotting([[0, 2]]) == 0
    assert mod.oranges_rotting([[1]]) == -1
    assert mod.oranges_rotting([[2]]) == 0
    assert mod.oranges_rotting([[0]]) == 0
    assert mod.oranges_rotting([]) == 0
    assert mod.oranges_rotting([[2, 1], [1, 1]]) == 2


def test_decode_ways():
    mod = load("dynamic_programming/decode_ways.py")
    assert mod.num_decodings("12") == 2
    assert mod.num_decodings("226") == 3
    assert mod.num_decodings("11106") == 2
    assert mod.num_decodings("10") == 1
    assert mod.num_decodings("27") == 1
    assert mod.num_decodings("1") == 1
    # No-solution / invalid encodings
    assert mod.num_decodings("06") == 0
    assert mod.num_decodings("0") == 0
    assert mod.num_decodings("100") == 0
    assert mod.num_decodings("") == 0


def test_course_schedule_ii():
    mod = load("advanced_graphs/course_schedule_ii.py")

    def is_valid(order, n, prereqs):
        if len(order) != n or sorted(order) != list(range(n)):
            return False
        pos = {c: i for i, c in enumerate(order)}
        return all(pos[b] < pos[a] for a, b in prereqs)

    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert is_valid(mod.find_order(4, prereqs), 4, prereqs)
    assert mod.find_order(2, [[1, 0]]) == [0, 1]
    # No-solution: a cycle yields an empty list, never a partial order
    assert mod.find_order(2, [[1, 0], [0, 1]]) == []
    assert mod.find_order(3, [[0, 1], [1, 2], [2, 0]]) == []
    # Edge cases: no prerequisites, single course, no courses
    assert is_valid(mod.find_order(3, []), 3, [])
    assert mod.find_order(1, []) == [0]
    assert mod.find_order(0, []) == []


def test_pacific_atlantic_water_flow():
    mod = load("graphs/pacific_atlantic_water_flow.py")
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    assert mod.pacific_atlantic(heights) == [
        [0, 4],
        [1, 3],
        [1, 4],
        [2, 2],
        [3, 0],
        [3, 1],
        [4, 0],
    ]
    # Single cell touches both oceans; a flat plateau drains everywhere
    assert mod.pacific_atlantic([[1]]) == [[0, 0]]
    assert mod.pacific_atlantic([[1, 1], [1, 1]]) == [[0, 0], [0, 1], [1, 0], [1, 1]]
    # Strictly rising towards the Atlantic corner: only that corner
    # and the Pacific borders that can climb to it qualify
    assert mod.pacific_atlantic([[2, 1], [1, 2]]) == [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert mod.pacific_atlantic([]) == []
    assert mod.pacific_atlantic([[]]) == []


def test_lowest_common_ancestor():
    mod = load("trees/lowest_common_ancestor.py")
    n7, n4 = mod.TreeNode(7), mod.TreeNode(4)
    n6, n2 = mod.TreeNode(6), mod.TreeNode(2, n7, n4)
    n5, n1 = mod.TreeNode(5, n6, n2), mod.TreeNode(1, mod.TreeNode(0), mod.TreeNode(8))
    root = mod.TreeNode(3, n5, n1)
    assert mod.lowest_common_ancestor(root, n5, n1) is root
    # A node is its own descendant: ancestor on the path wins
    assert mod.lowest_common_ancestor(root, n5, n4) is n5
    assert mod.lowest_common_ancestor(root, n7, n4) is n2
    assert mod.lowest_common_ancestor(root, n6, n4) is n5
    assert mod.lowest_common_ancestor(root, root, n4) is root
    # Edge cases: empty tree, same node twice, single-node tree
    assert mod.lowest_common_ancestor(None, n5, n1) is None
    assert mod.lowest_common_ancestor(root, n5, n5) is n5
    solo = mod.TreeNode(1)
    assert mod.lowest_common_ancestor(solo, solo, solo) is solo


def test_binary_tree_right_side_view():
    mod = load("trees/binary_tree_right_side_view.py")
    tree = mod.TreeNode(
        1,
        mod.TreeNode(2, None, mod.TreeNode(5)),
        mod.TreeNode(3, None, mod.TreeNode(4)),
    )
    assert mod.right_side_view(tree) == [1, 3, 4]
    assert mod.right_side_view(mod.TreeNode(1, None, mod.TreeNode(3))) == [1, 3]
    # A deeper left subtree shows through where the right side ends
    deep_left = mod.TreeNode(1, mod.TreeNode(2, mod.TreeNode(4)), mod.TreeNode(3))
    assert mod.right_side_view(deep_left) == [1, 3, 4]
    # Edge cases: empty tree, single node, left spine only
    assert mod.right_side_view(None) == []
    assert mod.right_side_view(mod.TreeNode(1)) == [1]
    spine = mod.TreeNode(1, mod.TreeNode(2, mod.TreeNode(3)))
    assert mod.right_side_view(spine) == [1, 2, 3]


# --- Intervals -------------------------------------------------------------

def test_merge_intervals():
    mod = load("intervals/merge_intervals.py")
    assert mod.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    # Touching endpoints merge
    assert mod.merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    # Unsorted input comes back sorted; nested intervals are absorbed
    assert mod.merge_intervals([[8, 10], [1, 3], [2, 6]]) == [[1, 6], [8, 10]]
    assert mod.merge_intervals([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]
    assert mod.merge_intervals([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
    # Edge cases: single interval, empty input
    assert mod.merge_intervals([[1, 4]]) == [[1, 4]]
    assert mod.merge_intervals([]) == []
    # Input must not be mutated
    data = [[2, 6], [1, 3]]
    mod.merge_intervals(data)
    assert data == [[2, 6], [1, 3]]


# --- Backtracking ----------------------------------------------------------

def test_combination_sum():
    mod = load("backtracking/combination_sum.py")
    assert mod.combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert mod.combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    # Input order does not change the combinations produced
    assert mod.combination_sum([7, 2, 6, 3], 7) == [[2, 2, 3], [7]]
    # No-solution: no combination reaches the target
    assert mod.combination_sum([2], 1) == []
    assert mod.combination_sum([4, 6], 5) == []
    # Edge cases: single exact candidate, empty candidates, zero target
    assert mod.combination_sum([5], 5) == [[5]]
    assert mod.combination_sum([], 5) == []
    assert mod.combination_sum([2, 3], 0) == [[]]


def test_insert_interval():
    mod = load("intervals/insert_interval.py")
    assert mod.insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert mod.insert_interval(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]
    # Disjoint inserts at the head, middle and tail keep the sort order
    assert mod.insert_interval([[3, 4], [6, 7]], [1, 2]) == [[1, 2], [3, 4], [6, 7]]
    assert mod.insert_interval([[1, 2], [6, 7]], [3, 4]) == [[1, 2], [3, 4], [6, 7]]
    assert mod.insert_interval([[1, 2], [3, 4]], [6, 7]) == [[1, 2], [3, 4], [6, 7]]
    # Touching endpoints merge; a covering interval absorbs everything
    assert mod.insert_interval([[1, 3], [5, 7]], [3, 5]) == [[1, 7]]
    assert mod.insert_interval([[2, 3], [5, 6]], [1, 10]) == [[1, 10]]
    # Edge cases: empty list, single interval
    assert mod.insert_interval([], [5, 7]) == [[5, 7]]
    assert mod.insert_interval([[1, 2]], [3, 4]) == [[1, 2], [3, 4]]
    # Inputs must not be mutated
    data, new = [[1, 3], [6, 9]], [2, 5]
    mod.insert_interval(data, new)
    assert data == [[1, 3], [6, 9]] and new == [2, 5]


def test_word_search():
    mod = load("backtracking/word_search.py")
    sample = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ]
    assert mod.exist([row[:] for row in sample], "ABCCED") is True
    assert mod.exist([row[:] for row in sample], "SEE") is True
    # No-solution: a cell cannot be reused within one word
    assert mod.exist([row[:] for row in sample], "ABCB") is False
    # Board is restored after the search
    board = [row[:] for row in sample]
    mod.exist(board, "ABCCED")
    assert board == sample
    # Edge cases: single cell, empty board, empty word, word longer than grid
    assert mod.exist([["a"]], "a") is True
    assert mod.exist([["a"]], "b") is False
    assert mod.exist([], "a") is False
    assert mod.exist([[]], "a") is False
    assert mod.exist([["a"]], "") is False
    assert mod.exist([["a", "b"]], "abc") is False


def test_kth_smallest_in_bst():
    mod = load("trees/kth_smallest_in_bst.py")
    tree = mod.TreeNode(3, mod.TreeNode(1, None, mod.TreeNode(2)), mod.TreeNode(4))
    assert mod.kth_smallest(tree, 1) == 1
    assert mod.kth_smallest(tree, 2) == 2
    assert mod.kth_smallest(tree, 4) == 4
    larger = mod.TreeNode(
        5,
        mod.TreeNode(3, mod.TreeNode(2, mod.TreeNode(1)), mod.TreeNode(4)),
        mod.TreeNode(6),
    )
    assert mod.kth_smallest(larger, 3) == 3
    assert mod.kth_smallest(larger, 6) == 6
    # Edge cases: single node, left spine only
    assert mod.kth_smallest(mod.TreeNode(1), 1) == 1
    spine = mod.TreeNode(3, mod.TreeNode(2, mod.TreeNode(1)))
    assert mod.kth_smallest(spine, 3) == 3
    # Out-of-range k raises instead of returning a wrong value
    import pytest

    with pytest.raises(ValueError):
        mod.kth_smallest(None, 1)
    with pytest.raises(ValueError):
        mod.kth_smallest(tree, 0)
    with pytest.raises(ValueError):
        mod.kth_smallest(tree, 5)


def test_permutations():
    mod = load("backtracking/permutations.py")
    assert mod.permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert mod.permute([0, 1]) == [[0, 1], [1, 0]]
    # Count check: 4 distinct values give 4! unique orderings
    perms = mod.permute([1, 2, 3, 4])
    assert len(perms) == 24 and len({tuple(p) for p in perms}) == 24
    # Edge cases: single element, empty input
    assert mod.permute([1]) == [[1]]
    assert mod.permute([]) == [[]]
    # Input order drives output order; input itself is not mutated
    data = [2, 1]
    assert mod.permute(data) == [[2, 1], [1, 2]]
    assert data == [2, 1]


def test_time_based_key_value_store():
    mod = load("design/time_based_key_value_store.py")
    store = mod.TimeMap()
    store.set("foo", "bar", 1)
    assert store.get("foo", 1) == "bar"
    assert store.get("foo", 3) == "bar"
    store.set("foo", "bar2", 4)
    assert store.get("foo", 4) == "bar2"
    assert store.get("foo", 5) == "bar2"
    # Before the first version, and for unknown keys, the result is ""
    assert store.get("foo", 0) == ""
    assert store.get("missing", 10) == ""
    # Keys are independent; an in-between timestamp floors to the prior set
    store.set("love", "high", 10)
    store.set("love", "low", 20)
    assert store.get("love", 15) == "high"
    assert store.get("love", 20) == "low"
    assert store.get("foo", 5) == "bar2"
    # A fresh store has nothing for any key
    assert mod.TimeMap().get("anything", 100) == ""


def test_task_scheduler():
    mod = load("heap/task_scheduler.py")
    assert mod.least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert mod.least_interval(["A", "A", "A", "B", "B", "B"], 3) == 10
    assert mod.least_interval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert mod.least_interval(["A", "A", "B", "B", "C", "C"], 1) == 6
    # No cooling: every slot is work
    assert mod.least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6
    # A single repeated task forces (count - 1) * (n + 1) + 1 slots
    assert mod.least_interval(["A", "A", "A"], 2) == 7
    assert mod.least_interval(["A", "A"], 2) == 4
    # Edge cases: empty input, single task
    assert mod.least_interval([], 2) == 0
    assert mod.least_interval(["A"], 5) == 1


def test_rotate_image():
    mod = load("arrays/rotate_image.py")
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mod.rotate_image(data)
    assert data == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    larger = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    mod.rotate_image(larger)
    assert larger == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    # Rotating four times restores the original matrix
    spun = [[1, 2], [3, 4]]
    for _ in range(4):
        mod.rotate_image(spun)
    assert spun == [[1, 2], [3, 4]]
    # Edge cases: empty matrix, single cell
    empty = []
    mod.rotate_image(empty)
    assert empty == []
    single = [[1]]
    mod.rotate_image(single)
    assert single == [[1]]


def test_meeting_rooms():
    mod = load("intervals/meeting_rooms.py")
    assert mod.can_attend_meetings([[0, 30], [5, 10], [15, 20]]) is False
    assert mod.can_attend_meetings([[7, 10], [2, 4]]) is True
    # Touching endpoints do not overlap
    assert mod.can_attend_meetings([[0, 5], [5, 10], [10, 15]]) is True
    # Unsorted input; a fully nested meeting still overlaps
    assert mod.can_attend_meetings([[15, 20], [0, 30]]) is False
    assert mod.can_attend_meetings([[1, 10], [2, 3]]) is False
    # Edge cases: empty input, single meeting
    assert mod.can_attend_meetings([]) is True
    assert mod.can_attend_meetings([[1, 4]]) is True
    # Input must not be mutated
    data = [[7, 10], [2, 4]]
    mod.can_attend_meetings(data)
    assert data == [[7, 10], [2, 4]]


def test_spiral_matrix():
    mod = load("arrays/spiral_matrix.py")
    assert mod.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert mod.spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7,
    ]
    assert mod.spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert mod.spiral_order([[1, 2, 3]]) == [1, 2, 3]
    assert mod.spiral_order([[1], [2], [3]]) == [1, 2, 3]
    # Edge cases: empty matrix, empty row, single cell
    assert mod.spiral_order([]) == []
    assert mod.spiral_order([[]]) == []
    assert mod.spiral_order([[7]]) == [7]
    # Input must not be mutated
    data = [[1, 2], [3, 4]]
    mod.spiral_order(data)
    assert data == [[1, 2], [3, 4]]


def test_set_matrix_zeroes():
    mod = load("arrays/set_matrix_zeroes.py")
    data = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    mod.set_zeroes(data)
    assert data == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    larger = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    mod.set_zeroes(larger)
    assert larger == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    # No zeroes: matrix is unchanged
    clean = [[1, 2], [3, 4]]
    mod.set_zeroes(clean)
    assert clean == [[1, 2], [3, 4]]
    # Zero in the first row / first column only
    edge = [[0, 2], [3, 4]]
    mod.set_zeroes(edge)
    assert edge == [[0, 0], [0, 4]]
    # Edge cases: empty matrix, single cell (zero and non-zero)
    empty = []
    mod.set_zeroes(empty)
    assert empty == []
    single = [[0]]
    mod.set_zeroes(single)
    assert single == [[0]]
    one = [[5]]
    mod.set_zeroes(one)
    assert one == [[5]]


def test_subsets():
    mod = load("backtracking/subsets.py")
    assert mod.subsets([1, 2, 3]) == [
        [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3],
    ]
    assert mod.subsets([0]) == [[], [0]]
    # Count check: n distinct values give exactly 2^n subsets, no duplicates
    result = mod.subsets([1, 2, 3, 4])
    assert len(result) == 16
    assert len({tuple(s) for s in result}) == 16
    # Edge cases: empty input, single element
    assert mod.subsets([]) == [[]]
    assert mod.subsets([5]) == [[], [5]]
    # Input must not be mutated
    data = [2, 1]
    assert mod.subsets(data) == [[], [2], [2, 1], [1]]
    assert data == [2, 1]


def test_partition_equal_subset_sum():
    mod = load("advanced_dp/partition_equal_subset_sum.py")
    assert mod.can_partition([1, 5, 11, 5]) is True
    assert mod.can_partition([1, 2, 3, 5]) is False
    assert mod.can_partition([1, 2, 5]) is False
    assert mod.can_partition([2, 2, 3, 5]) is False
    assert mod.can_partition([3, 3, 3, 4, 5]) is True
    # Odd total can never be partitioned
    assert mod.can_partition([1, 2, 4]) is False
    # Edge cases: empty input, single element, two equal elements
    assert mod.can_partition([]) is True
    assert mod.can_partition([100]) is False
    assert mod.can_partition([1, 1]) is True
    assert mod.can_partition([2, 2]) is True


def test_generate_parentheses():
    mod = load("backtracking/generate_parentheses.py")
    assert mod.generate_parenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert mod.generate_parenthesis(1) == ["()"]
    assert mod.generate_parenthesis(2) == ["(())", "()()"]
    # Count is the nth Catalan number; every result is balanced and unique
    result4 = mod.generate_parenthesis(4)
    assert len(result4) == 14
    assert len(set(result4)) == 14
    assert all(len(s) == 8 for s in result4)
    # Edge cases: zero pairs, negative input
    assert mod.generate_parenthesis(0) == [""]
    assert mod.generate_parenthesis(-1) == []


def test_koko_eating_bananas():
    mod = load("binary_search/koko_eating_bananas.py")
    assert mod.min_eating_speed([3, 6, 7, 11], 8) == 4
    assert mod.min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert mod.min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert mod.min_eating_speed([1, 1, 1, 999999999], 10) == 142857143
    # Edge cases: empty input, single pile
    assert mod.min_eating_speed([], 5) == 0
    assert mod.min_eating_speed([5], 5) == 1
    assert mod.min_eating_speed([5], 1) == 5
    # No-solution: fewer hours than piles can never finish
    assert mod.min_eating_speed([3, 6, 7, 11], 3) == -1
    # Input must not be mutated
    data = [3, 6, 7, 11]
    mod.min_eating_speed(data, 8)
    assert data == [3, 6, 7, 11]


def test_non_overlapping_intervals():
    mod = load("intervals/non_overlapping_intervals.py")
    assert mod.erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert mod.erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert mod.erase_overlap_intervals([[1, 2], [2, 3]]) == 0
    assert mod.erase_overlap_intervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
    # Edge cases: empty input, single interval, touching endpoints
    assert mod.erase_overlap_intervals([]) == 0
    assert mod.erase_overlap_intervals([[1, 4]]) == 0
    assert mod.erase_overlap_intervals([[3, 4], [1, 2], [2, 3]]) == 0
    # Input must not be mutated
    data = [[2, 3], [1, 2]]
    mod.erase_overlap_intervals(data)
    assert data == [[2, 3], [1, 2]]


def test_longest_repeating_character_replacement():
    mod = load("sliding_window/longest_repeating_character_replacement.py")
    assert mod.character_replacement("ABAB", 2) == 4
    assert mod.character_replacement("AABABBA", 1) == 4
    assert mod.character_replacement("AAAA", 0) == 4
    assert mod.character_replacement("ABCDE", 1) == 2
    assert mod.character_replacement("BAAAB", 2) == 5
    # Edge cases: empty string, single character
    assert mod.character_replacement("", 3) == 0
    assert mod.character_replacement("A", 0) == 1
    # No-solution sentinel: a negative budget can never be satisfied
    assert mod.character_replacement("ABAB", -1) == -1


def test_diameter_of_binary_tree():
    mod = load("trees/diameter_of_binary_tree.py")
    tree = mod.TreeNode(
        1,
        mod.TreeNode(2, mod.TreeNode(4), mod.TreeNode(5)),
        mod.TreeNode(3),
    )
    assert mod.diameter_of_binary_tree(tree) == 3
    assert mod.diameter_of_binary_tree(mod.TreeNode(1, mod.TreeNode(2))) == 1
    # Longest path need not pass through the root
    skewed = mod.TreeNode(
        1,
        mod.TreeNode(
            2,
            mod.TreeNode(3, mod.TreeNode(4, mod.TreeNode(5))),
            mod.TreeNode(6),
        ),
    )
    assert mod.diameter_of_binary_tree(skewed) == 4
    # Edge cases: empty tree, single node, straight chain
    assert mod.diameter_of_binary_tree(None) == 0
    assert mod.diameter_of_binary_tree(mod.TreeNode(1)) == 0
    chain = mod.TreeNode(1, mod.TreeNode(2, mod.TreeNode(3, mod.TreeNode(4))))
    assert mod.diameter_of_binary_tree(chain) == 3


def test_unique_paths():
    mod = load("dynamic_programming/unique_paths.py")
    assert mod.unique_paths(3, 7) == 28
    assert mod.unique_paths(3, 2) == 3
    assert mod.unique_paths(3, 3) == 6
    # Symmetry: transposing the grid cannot change the count
    assert mod.unique_paths(7, 3) == 28
    assert mod.unique_paths(4, 4) == 20
    # Edge cases: single cell, single row/column, degenerate grids
    assert mod.unique_paths(1, 1) == 1
    assert mod.unique_paths(1, 10) == 1
    assert mod.unique_paths(10, 1) == 1
    assert mod.unique_paths(0, 5) == 0
    assert mod.unique_paths(5, 0) == 0
    assert mod.unique_paths(-2, 3) == 0


def test_longest_consecutive_sequence():
    mod = load("hashmaps/longest_consecutive_sequence.py")
    assert mod.longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert mod.longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert mod.longest_consecutive([1, 0, 1, 2]) == 3
    assert mod.longest_consecutive([9, 8, 7, 6, 5]) == 5
    # Edge cases: empty input, single element, duplicates, negatives
    assert mod.longest_consecutive([]) == 0
    assert mod.longest_consecutive([7]) == 1
    assert mod.longest_consecutive([5, 5, 5]) == 1
    assert mod.longest_consecutive([-3, -2, -1, 1, 2]) == 3
    # No-solution analogue: no two values are consecutive
    assert mod.longest_consecutive([10, 30, 50]) == 1
    # Input must not be mutated
    data = [100, 4, 200, 1, 3, 2]
    mod.longest_consecutive(data)
    assert data == [100, 4, 200, 1, 3, 2]


def test_find_minimum_in_rotated_sorted_array():
    mod = load("binary_search/find_minimum_in_rotated_sorted_array.py")
    assert mod.find_min([3, 4, 5, 1, 2]) == 1
    assert mod.find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert mod.find_min([11, 13, 15, 17]) == 11
    assert mod.find_min([2, 3, 4, 5, 1]) == 1
    assert mod.find_min([-5, -2, 0, -10, -7]) == -10
    # Edge cases: empty input, single element, two elements
    assert mod.find_min([]) is None
    assert mod.find_min([1]) == 1
    assert mod.find_min([2, 1]) == 1
    assert mod.find_min([1, 2]) == 1
    # Input must not be mutated
    data = [4, 5, 6, 7, 0, 1, 2]
    mod.find_min(data)
    assert data == [4, 5, 6, 7, 0, 1, 2]


def test_word_ladder():
    mod = load("graphs/word_ladder.py")
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert mod.ladder_length("hit", "cog", words) == 5
    assert mod.ladder_length("hit", "cog", ["hot", "dot", "tog", "cog"]) == 0
    assert mod.ladder_length("a", "c", ["a", "b", "c"]) == 2
    assert mod.ladder_length("hot", "dog", ["hot", "dog", "dot"]) == 3
    # Edge cases: empty inputs, identical begin/end, end not in list
    assert mod.ladder_length("", "cog", ["cog"]) == 0
    assert mod.ladder_length("hit", "", ["hit"]) == 0
    assert mod.ladder_length("hit", "hit", ["hit"]) == 0
    assert mod.ladder_length("hit", "cog", []) == 0
    assert mod.ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    # Input must not be mutated
    data = ["hot", "dot", "dog", "lot", "log", "cog"]
    mod.ladder_length("hit", "cog", data)
    assert data == ["hot", "dot", "dog", "lot", "log", "cog"]


def test_n_queens():
    mod = load("backtracking/n_queens.py")
    assert mod.solve_n_queens(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert mod.solve_n_queens(1) == [["Q"]]
    # No-solution cases: 2 and 3 queens can never be placed safely
    assert mod.solve_n_queens(2) == []
    assert mod.solve_n_queens(3) == []
    # Known solution counts
    assert len(mod.solve_n_queens(5)) == 10
    assert len(mod.solve_n_queens(6)) == 4
    # Every 5-queens solution is a valid, non-attacking placement
    for sol in mod.solve_n_queens(5):
        assert len(sol) == 5 and all(len(row) == 5 for row in sol)
        assert sum(row.count("Q") for row in sol) == 5
    # Edge cases: degenerate board sizes
    assert mod.solve_n_queens(0) == []
    assert mod.solve_n_queens(-3) == []


def test_trapping_rain_water():
    import pytest

    mod = load("two_pointers/trapping_rain_water.py")
    assert mod.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert mod.trap([4, 2, 0, 3, 2, 5]) == 9
    assert mod.trap([3, 0, 3]) == 3
    assert mod.trap([2, 0, 2]) == 2
    # No-solution analogue: monotonic or flat maps trap nothing
    assert mod.trap([1, 2, 3, 4]) == 0
    assert mod.trap([4, 3, 2, 1]) == 0
    assert mod.trap([2, 2, 2]) == 0
    # Edge cases: empty input, single bar
    assert mod.trap([]) == 0
    assert mod.trap([5]) == 0
    with pytest.raises(ValueError):
        mod.trap([1, -1, 2])
    # Input must not be mutated
    data = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    mod.trap(data)
    assert data == [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def test_largest_rectangle_in_histogram():
    import pytest

    mod = load("stack/largest_rectangle_in_histogram.py")
    assert mod.largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert mod.largest_rectangle_area([2, 4]) == 4
    assert mod.largest_rectangle_area([5, 5, 5]) == 15
    assert mod.largest_rectangle_area([1, 2, 3, 4, 5]) == 9
    assert mod.largest_rectangle_area([5, 4, 3, 2, 1]) == 9
    assert mod.largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]) == 12
    # Edge cases: empty input, single bar, all zeroes
    assert mod.largest_rectangle_area([]) == 0
    assert mod.largest_rectangle_area([7]) == 7
    assert mod.largest_rectangle_area([0, 0, 0]) == 0
    with pytest.raises(ValueError):
        mod.largest_rectangle_area([2, -1])
    # Input must not be mutated
    data = [2, 1, 5, 6, 2, 3]
    mod.largest_rectangle_area(data)
    assert data == [2, 1, 5, 6, 2, 3]


def test_palindromic_substrings():
    mod = load("dynamic_programming/palindromic_substrings.py")
    assert mod.count_substrings("abc") == 3
    assert mod.count_substrings("aaa") == 6
    assert mod.count_substrings("abba") == 6
    assert mod.count_substrings("racecar") == 10
    assert mod.count_substrings("aa") == 3
    assert mod.count_substrings("ab") == 2
    # Edge cases: empty string, single character
    assert mod.count_substrings("") == 0
    assert mod.count_substrings("a") == 1


def test_surrounded_regions():
    mod = load("graphs/surrounded_regions.py")
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    assert mod.solve(board) == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    # Input must not be mutated
    assert board[1][1] == "O"
    # Border regions survive entirely
    assert mod.solve([["O", "O"], ["O", "O"]]) == [["O", "O"], ["O", "O"]]
    assert mod.solve([["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"]]) == [
        ["X", "O", "X"],
        ["X", "O", "X"],
        ["X", "X", "X"],
    ]
    # Edge cases: empty board, single cell
    assert mod.solve([]) == []
    assert mod.solve([[]]) == [[]]
    assert mod.solve([["O"]]) == [["O"]]
    assert mod.solve([["X"]]) == [["X"]]


def test_evaluate_reverse_polish_notation():
    mod = load("stack/evaluate_reverse_polish_notation.py")
    assert mod.eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert mod.eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert mod.eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    # Division truncates toward zero, in both signs
    assert mod.eval_rpn(["7", "2", "/"]) == 3
    assert mod.eval_rpn(["-7", "2", "/"]) == -3
    assert mod.eval_rpn(["7", "-2", "/"]) == -3
    # Operand order for subtraction and division
    assert mod.eval_rpn(["3", "5", "-"]) == -2
    assert mod.eval_rpn(["2", "6", "/"]) == 0
    # Edge cases: single value, single negative value, malformed input
    assert mod.eval_rpn(["42"]) == 42
    assert mod.eval_rpn(["-11"]) == -11
    import pytest

    for bad in ([], ["1", "+"], ["1", "2"], ["1", "x", "+"]):
        with pytest.raises(ValueError):
            mod.eval_rpn(bad)


def test_meeting_rooms_ii():
    mod = load("intervals/meeting_rooms_ii.py")
    assert mod.min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert mod.min_meeting_rooms([[7, 10], [2, 4]]) == 1
    # Touching endpoints can share a room
    assert mod.min_meeting_rooms([[0, 5], [5, 10], [10, 15]]) == 1
    # Fully nested meetings each need their own room
    assert mod.min_meeting_rooms([[1, 10], [2, 9], [3, 8]]) == 3
    assert mod.min_meeting_rooms([[15, 20], [0, 10], [5, 12], [11, 16]]) == 2
    assert mod.min_meeting_rooms([[1, 5], [1, 5], [1, 5]]) == 3
    # Edge cases: empty input, single meeting
    assert mod.min_meeting_rooms([]) == 0
    assert mod.min_meeting_rooms([[1, 4]]) == 1
    # Input must not be mutated
    data = [[7, 10], [2, 4]]
    mod.min_meeting_rooms(data)
    assert data == [[7, 10], [2, 4]]


def test_binary_tree_zigzag_level_order_traversal():
    mod = load("trees/binary_tree_zigzag_level_order_traversal.py")
    tree = mod.TreeNode(3, mod.TreeNode(9), mod.TreeNode(20, mod.TreeNode(15), mod.TreeNode(7)))
    assert mod.zigzag_level_order(tree) == [[3], [20, 9], [15, 7]]
    deep = mod.TreeNode(
        1,
        mod.TreeNode(2, mod.TreeNode(4), mod.TreeNode(5)),
        mod.TreeNode(3, mod.TreeNode(6), mod.TreeNode(7)),
    )
    assert mod.zigzag_level_order(deep) == [[1], [3, 2], [4, 5, 6, 7]]
    # A left-only chain reads one value per level, direction irrelevant
    chain = mod.TreeNode(1, mod.TreeNode(2, mod.TreeNode(3)))
    assert mod.zigzag_level_order(chain) == [[1], [2], [3]]
    # Edge cases: empty tree, single node
    assert mod.zigzag_level_order(None) == []
    assert mod.zigzag_level_order(mod.TreeNode(42)) == [[42]]


def test_word_dictionary():
    mod = load("tries/word_dictionary.py")
    dictionary = mod.WordDictionary()
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
    empty = mod.WordDictionary()
    assert empty.search("a") is False
    assert empty.search(".") is False
    assert empty.search("") is False
    dictionary.add_word("bad")
    assert dictionary.search("bad") is True
