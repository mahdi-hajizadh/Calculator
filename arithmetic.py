"""Evaluate the arithmetic operators supported by the calculator UI."""

import ast
import math
import operator

BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}
UNARY_OPERATORS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def calculate_expression(expression):
    if len(expression) > 256:
        raise ValueError("Expression is too long")
    return _evaluate(ast.parse(expression.strip(), mode="eval").body)


def _evaluate(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        result = node.value
    elif isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPERATORS:
        result = BINARY_OPERATORS[type(node.op)](_evaluate(node.left), _evaluate(node.right))
    elif isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPERATORS:
        result = UNARY_OPERATORS[type(node.op)](_evaluate(node.operand))
    else:
        raise ValueError("Unsupported arithmetic expression")

    if isinstance(result, float) and not math.isfinite(result):
        raise ValueError("Result must be finite")
    return result
