Certainly! When evaluating user input, it's important to safely parse the expression and ensure that no arbitrary code execution is possible. We will use Python's abstract syntax tree (AST) to safely evaluate mathematical expressions. Here's how you can accomplish this:

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
    Safely evaluates a math expression provided as a string.
    Only basic arithmetic operations are allowed.
    """
    try:
        node = ast.parse(user_input, mode='eval').body
    except (SyntaxError, ValueError):
        raise ValueError("Invalid expression")

    def _evaluate(node):
        """ Recursively evaluate an AST node """
        if isinstance(node, ast.BinOp):
            left = _evaluate(node.left)
            right = _evaluate(node.right)
            op_type = type(node.op)
            if op_type in ALLOWED_OPERATORS:
                return ALLOWED_OPERATORS[op_type](left, right)
        elif isinstance(node, ast.UnaryOp): # Handle unary operators (e.g., -)
            operand = _evaluate(node.operand)
            op_type = type(node.op)
            if op_type in ALLOWED_OPERATORS:
                return ALLOWED_OPERATORS[op_type](operand)
        elif isinstance(node, ast.Num):  # Ensure the node is a number
            return node.n
        else:
            raise ValueError("Unsupported expression")
    
    return _evaluate(node)


- We use the `ast` module to parse the input into an abstract syntax tree (AST), which ensures structured parsing and avoids execution of arbitrary code.
- Only specific AST node types and operations (`Add`, `Sub`, `Mult`, `Div`, `Pow`, `Mod`, and `USub`) are allowed; all others will raise an exception, providing a safeguard against malicious inputs.
- Recursive evaluation is performed by the `_evaluate` function, ensuring only known and explicitly allowed operations are executed. Otherwise, any unsupported nodes raise a `ValueError`.