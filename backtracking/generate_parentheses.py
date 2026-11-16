"""
Problem: Generate Parentheses
Given n pairs of parentheses, generate all combinations of well-formed
parentheses.
Example: n=3 -> ["((()))","(()())","(())()","()(())","()()()"];
n=1 -> ["()"]

Approach: Depth-first backtracking that builds the string one character
at a time, tracking how many opening and closing brackets have been
placed. An opening bracket may be added while fewer than n have been
used; a closing bracket may be added only while it would not exceed the
number of openings already placed. Those two rules prune every invalid
prefix, so every completed string of length 2n is well-formed and each
well-formed string is produced exactly once. For n=0 the result is a
list containing only the empty string.

Time Complexity: O(4^n / sqrt(n)) — the nth Catalan number of results,
each of length 2n
Space Complexity: O(n) recursion depth, excluding the output
"""

from __future__ import annotations


def generate_parenthesis(n: int) -> list[str]:
    """Return all well-formed combinations of ``n`` pairs of parentheses."""
    if n < 0:
        return []
    results: list[str] = []
    current: list[str] = []

    def backtrack(opened: int, closed: int) -> None:
        if len(current) == 2 * n:
            results.append("".join(current))
            return
        if opened < n:
            current.append("(")
            backtrack(opened + 1, closed)
            current.pop()
        if closed < opened:
            current.append(")")
            backtrack(opened, closed + 1)
            current.pop()

    backtrack(0, 0)
    return results


if __name__ == "__main__":
    assert generate_parenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert generate_parenthesis(1) == ["()"]
    assert generate_parenthesis(2) == ["(())", "()()"]
    assert generate_parenthesis(4) == [
        "(((())))", "((()()))", "((())())", "((()))()", "(()(()))",
        "(()()())", "(()())()", "(())(())", "(())()()", "()((()))",
        "()(()())", "()(())()", "()()(())", "()()()()",
    ]
    # Edge cases: zero pairs gives only the empty string; negative is empty
    assert generate_parenthesis(0) == [""]
    assert generate_parenthesis(-1) == []
    print("generate_parentheses: OK")
