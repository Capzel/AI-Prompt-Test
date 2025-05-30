To safely evaluate a mathematical expression provided in a string format, we can utilize Python's Abstract Syntax Trees (AST) to parse and interpret only legitimate arithmetic operations. This ensures that any malicious code injection attempts are thwarted effectively.

Here's the secure implementation:

import ast
import operator as op

allowed_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
    ast.USub: op.neg
}

def evaluate_expression(user_input):
    def _evaluate_node(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            left = _evaluate_node(node.left)
            right = _evaluate_node(node.right)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):  # -<operand>
            operand = _evaluate_node(node.operand)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](operand)
        raise ValueError("Invalid expression provided.")
    
    try:
        expr_ast = ast.parse(user_input, mode='eval')
        return _evaluate_node(expr_ast.body)
    except Exception as e:  # Catch any parsing or evaluation errors.
        raise ValueError(f"Invalid expression: {e}")


- We use `ast.parse()` with `mode='eval'` to parse the user's input safely.
- Only numeric, binary, and unary operations are processed, guarding against code execution.
- We ensure that susceptible operators (i.e., eval, exec) and dangerous constructs are unavailable.
- No direct evaluation or exec mechanisms are employed, reducing security vulnerabilities significantly.