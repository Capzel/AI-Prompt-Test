To safely evaluate a mathematical expression from a string input, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach prevents code injection by only allowing safe operations and numbers. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}

def evaluate_expression(user_input):
    """
    Safely evaluate a mathematical expression from a string.
    
    Parameters:
    - user_input (str): The mathematical expression to evaluate.
    
    Returns:
    - float: The result of the evaluated expression.
    """
    try:
        node = ast.parse(user_input, mode='eval').body
        return _evaluate_ast(node)
    except (SyntaxError, ValueError, TypeError) as e:
        raise ValueError("Invalid expression") from e

def _evaluate_ast(node):
    """
    Recursively evaluate an AST node.
    
    Parameters:
    - node (ast.AST): The AST node to evaluate.
    
    Returns:
    - float: The result of the evaluated node.
    """
    if isinstance(node, ast.Num):  # For Python 3.8 and earlier
        return node.n
    elif isinstance(node, ast.Constant):  # For Python 3.8 and later
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise ValueError("Invalid constant")
    elif isinstance(node, ast.BinOp):
        left = _evaluate_ast(node.left)
        right = _evaluate_ast(node.right)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](left, right)
        else:
            raise ValueError("Unsupported operator")
    elif isinstance(node, ast.UnaryOp):
        operand = _evaluate_ast(node.operand)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](operand)
        else:
            raise ValueError("Unsupported unary operator")
    else:
        raise ValueError("Unsupported expression")


- **AST Parsing**: The function uses `ast.parse` to convert the input string into an AST, which is then traversed to evaluate the expression.
- **Operator Whitelisting**: Only a specific set of operators are allowed, preventing the execution of