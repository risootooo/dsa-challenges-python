"""
Problem: Valid Parentheses
Given a string of brackets () [] {}, return True if it is well-formed:
open brackets are closed by the same type, in the correct order.
Example: "()[]{}" -> True, "(]" -> False

Approach: Push opening brackets onto a stack. For a closing bracket, the
top of the stack must be its matching opener; pop it. The stack must be
empty at the end.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from __future__ import annotations


def is_valid_parentheses(s: str) -> bool:
    """Return True if the bracket string ``s`` is well-formed."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    return not stack


if __name__ == "__main__":
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("([{}])") is True
    print("valid_parentheses: OK")
