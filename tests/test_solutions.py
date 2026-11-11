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
