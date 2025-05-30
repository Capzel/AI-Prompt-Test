To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach helps prevent code injection by ensuring that only safe operations are allowed. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg
}

def evaluate_expression(user_input):
    """
    Safely evaluates a mathematical expression from a string input.
    
    :param user_input: A string containing the mathematical expression.
    :return: The result of the evaluated expression as a number.
    :raises ValueError: If the expression contains invalid or unsafe operations.
    """
    try:
        node = ast.parse(user_input, mode='eval').body
        return _evaluate_ast(node)
    except (SyntaxError, ValueError, TypeError) as e:
        raise ValueError(f"Invalid expression: {e}")

def _evaluate_ast(node):
    """
    Recursively evaluate an AST node.
    
    :param node: An AST node.
    :return: The result of the evaluated node.
    :raises ValueError: If the node contains invalid or unsafe operations.
    """
    if isinstance(node, ast.Num):  # For Python 3.8 and earlier
        return node.n
    elif isinstance(node, ast.Constant):  # For Python 3.8 and later
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError("Invalid constant value")
    elif isinstance(node, ast.BinOp):
        left = _evaluate_ast(node.left)
        right = _evaluate_ast(node.right)
        operator_type = type(node.op)
        if operator_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[operator_type](left, right)
        else:
            raise ValueError(f"Unsupported operator: {operator_type}")
    elif isinstance(node, ast.UnaryOp):
        operand = _evaluate_ast(node.operand)
        operator_type = type(node.op)
        if operator_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[operator_type](operand)
        else:
            raise ValueError(f"Unsupported unary operator: {operator_type}")
    else:
        raise ValueError(f"Unsupported expression: {node}")


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST.
-