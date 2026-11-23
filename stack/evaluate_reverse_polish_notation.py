"""
Problem: Evaluate Reverse Polish Notation
Given a list of string tokens representing an arithmetic expression
in Reverse Polish (postfix) notation, evaluate it and return the
integer result. Valid operators are "+", "-", "*" and "/"; division
truncates toward zero. Operands may be negative, and the expression
is guaranteed valid with no division by zero.
Example: ["2","1","+","3","*"] -> 9 ((2 + 1) * 3);
["4","13","5","/","+"] -> 6 (4 + (13 / 5))

Approach: One left-to-right pass with a stack. A number token is
pushed; an operator pops the right operand then the left operand,
applies the operation, and pushes the result. Order matters for the
non-commutative operators, so the first value popped is the right
hand side. Division uses int(left / right) semantics without floats:
take the absolute quotient and restore the sign, which truncates
toward zero for arbitrarily large integers. An empty token list, an
unknown token, or a stack that does not end with exactly one value
raises ValueError — malformed input fails loudly, not silently.

Time Complexity: O(n) — each token is processed once
Space Complexity: O(n) for the stack
"""

from __future__ import annotations

_OPERATORS = {"+", "-", "*", "/"}


def _apply(operator: str, left: int, right: int) -> int:
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    # Division truncating toward zero, exact for big integers.
    quotient = abs(left) // abs(right)
    return quotient if (left < 0) == (right < 0) else -quotient


def eval_rpn(tokens: list[str]) -> int:
    """Evaluate the Reverse Polish Notation expression ``tokens``."""
    if not tokens:
        raise ValueError("tokens must not be empty")
    stack: list[int] = []
    for token in tokens:
        if token in _OPERATORS:
            if len(stack) < 2:
                raise ValueError(f"operator {token!r} lacks two operands")
            right = stack.pop()
            left = stack.pop()
            stack.append(_apply(token, left, right))
        else:
            try:
                stack.append(int(token))
            except ValueError:
                raise ValueError(f"unknown token: {token!r}") from None
    if len(stack) != 1:
        raise ValueError("expression does not reduce to a single value")
    return stack[0]


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    # Division truncates toward zero, in both signs
    assert eval_rpn(["7", "2", "/"]) == 3
    assert eval_rpn(["-7", "2", "/"]) == -3
    assert eval_rpn(["7", "-2", "/"]) == -3
    # Operand order for subtraction and division
    assert eval_rpn(["3", "5", "-"]) == -2
    assert eval_rpn(["2", "6", "/"]) == 0
    # Edge cases: single value, single negative value
    assert eval_rpn(["42"]) == 42
    assert eval_rpn(["-11"]) == -11
    for bad in ([], ["1", "+"], ["1", "2"], ["1", "x", "+"]):
        try:
            eval_rpn(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"malformed input must raise ValueError: {bad!r}")
    print("evaluate_reverse_polish_notation: OK")
