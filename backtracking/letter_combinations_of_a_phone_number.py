"""
Problem: Letter Combinations of a Phone Number
Given a string of digits 2-9, return every letter combination the
digits could represent on a telephone keypad (2=abc, 3=def, 4=ghi,
5=jkl, 6=mno, 7=pqrs, 8=tuv, 9=wxyz), in keypad order.
Example: "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Approach: Backtracking over the digit positions. A path holds one
chosen letter per digit processed so far; at each position, try every
letter on that digit's key in order, recurse to the next position,
then undo the choice. When the path covers every digit it is one
complete combination and is recorded. Digits outside 2-9 have no
letters and raise ValueError rather than silently producing nothing.

Time Complexity: O(4^n * n), n = number of digits (4 = largest key)
Space Complexity: O(n) recursion depth, excluding the output
"""

from __future__ import annotations

_KEYPAD: dict[str, str] = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations(digits: str) -> list[str]:
    """Return every keypad letter combination for `digits` (2-9)."""
    if not digits:
        return []
    for digit in digits:
        if digit not in _KEYPAD:
            raise ValueError(f"digit {digit!r} has no keypad letters")
    combinations: list[str] = []
    path: list[str] = []

    def backtrack(index: int) -> None:
        if index == len(digits):
            combinations.append("".join(path))
            return
        for letter in _KEYPAD[digits[index]]:
            path.append(letter)
            backtrack(index + 1)
            path.pop()

    backtrack(0)
    return combinations


if __name__ == "__main__":
    assert letter_combinations("23") == [
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf",
    ]
    assert letter_combinations("2") == ["a", "b", "c"]
    # Four-letter keys: 7 and 9 each produce four combinations alone
    assert letter_combinations("7") == ["p", "q", "r", "s"]
    assert letter_combinations("79") == [
        "pw", "px", "py", "pz", "qw", "qx", "qy", "qz",
        "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz",
    ]
    # Edge cases: empty input, invalid digits raise
    assert letter_combinations("") == []
    for bad in ("1", "0", "2a"):
        try:
            letter_combinations(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"expected ValueError for {bad!r}")
    print("letter_combinations_of_a_phone_number: OK")
