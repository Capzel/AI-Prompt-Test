To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach prevents code injection by only allowing a subset of safe operations and expressions. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg
}

def evaluate_expression(user_input):
    """
    Safely evaluates a mathematical expression provided as a string.
    
    Parameters:
    - user_input (str): The mathematical expression to evaluate.
    
    Returns:
    - float: The result of the evaluated expression.
    """
    try:
        node = ast.parse(user_input, mode='eval')

        return _evaluate_ast(node.body)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

def _evaluate_ast(node):
    if isinstance(node, ast.Expression):
        return _evaluate_ast(node.body)
    elif isinstance(node, ast.Num):  # For Python 3.8 and earlier
        return node.n
    elif isinstance(node, ast.Constant):  # For Python 3.8 and later
        return node.value
    elif isinstance(node, ast.BinOp):
        left = _evaluate_ast(node.left)
        right = _evaluate_ast(node.right)
        op_type = type(node.op)
        if op_type in allowed_operators:
            return allowed_operators[op_type](left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = _evaluate_ast(node.operand)
        op_type = type(node.op)
        if op_type in allowed_operators:
            return allowed_operators[op_type](operand)
    raise ValueError("Unsupported expression")


- **AST Parsing**: The `ast.parse` function is used to parse the input string into an AST. We specify `mode='eval'` to ensure the input is treated as a single expression.
- **Allowed Operations**: We define a dictionary `allowed_operators` that maps AST operator nodes to their corresponding Python functions. This restricts the operations to only those explicitly allowed.
- **Recursive Evaluation**: The `_evaluate_ast` function recursively evaluates the AST nodes, handling numbers, binary operations, and unary operations.
- **Error Handling**: If the expression contains unsupported nodes or operations