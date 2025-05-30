To safely evaluate a mathematical expression provided as a string, you can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression without executing arbitrary code. This approach ensures that only safe operations are performed, thus mitigating the risk of code injection. Here's how you can implement this:

import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.BitXor: operator.xor,
    ast.USub: operator.neg,
}

def evaluate_expression(user_input):
    """
    Safely evaluates a mathematical expression from a string input.
    
    Parameters:
        user_input (str): The mathematical expression to evaluate.
    
    Returns:
        float: The result of the evaluated expression.
    
    Raises:
        ValueError: If the expression contains unsupported operations or syntax.
    """
    
    try:
        parsed_expr = ast.parse(user_input, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid syntax")

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        elif isinstance(node, ast.Num):  # For Python >=3.8, use ast.Constant
            return node.n
        elif isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](left, right)
            else:
                raise ValueError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in OPERATORS:
                return OPERATORS[op_type](operand)
            else:
                raise ValueError(f"Unsupported unary operator: {op_type}")
        else:
            raise ValueError("Unsupported expression")

    return _eval(parsed_expr.body)


- **AST Parsing**: We use the `ast.parse` function in 'eval' mode to safely parse the input expression.
- **Node Evaluation**: The `_eval` function recursively evaluates the AST nodes, handling numbers, binary operations, and unary operations.
- **Operator Safety**: Only a predefined set of operators is allowed, ensuring that no arbitrary code execution is possible.
- **Error Handling**: The function raises a `ValueError` if unsupported operations or syntax are encountered.