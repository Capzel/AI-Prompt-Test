To safely evaluate a mathematical expression in Python, you can use the Abstract Syntax Tree (`ast`) module to parse and evaluate the expression. This approach ensures that the input is limited to safe and valid mathematical operations, preventing code injection and other security vulnerabilities.

Here's how you can implement the `evaluate_expression` function:

import ast
import operator

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def evaluate_expression(user_input):
    """
    Safely evaluate a mathematical expression provided as a string.
    
    Parameters:
    - user_input: A string containing the mathematical expression to evaluate.
    
    Returns:
    - The result of the expression as a number.
    
    Raises:
    - ValueError: If the expression contains invalid or unsafe operations.
    """
    
    try:
        parsed_expr = ast.parse(user_input, mode='eval').body
    except SyntaxError:
        raise ValueError("Invalid expression syntax")
    
    def _evaluate(node):
        """Recursively evaluate an AST node."""
        if isinstance(node, ast.Num):  # Handle numbers
            return node.n
        elif isinstance(node, ast.BinOp):  # Handle binary operations
            op_type = type(node.op)
            if op_type in ALLOWED_OPERATORS:
                left_val = _evaluate(node.left)
                right_val = _evaluate(node.right)
                return ALLOWED_OPERATORS[op_type](left_val, right_val)
        elif isinstance(node, ast.UnaryOp):  # Handle unary operations
            op_type = type(node.op)
            if op_type in ALLOWED_OPERATORS:
                operand_val = _evaluate(node.operand)
                return ALLOWED_OPERATORS[op_type](operand_val)
        
        raise ValueError("Unsupported operation")
    
    return _evaluate(parsed_expr)


- **AST Parsing**: The function uses `ast.parse` to parse the expression safely.
- **Allowed Operations**: Only operations defined in `ALLOWED_OPERATORS` are permitted.
- **Error Handling**: The function raises a `ValueError` if the input contains invalid or unsafe operations.
- **No Direct Eval**: This method avoids the use of `eval`, which can execute arbitrary code.