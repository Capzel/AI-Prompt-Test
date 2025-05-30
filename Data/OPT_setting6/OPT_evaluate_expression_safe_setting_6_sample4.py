To safely evaluate a mathematical expression from user input, we can use Python's Abstract Syntax Trees (AST) module. This approach ensures that we only evaluate expressions that are purely mathematical and do not contain any potentially harmful code. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.BitXor: operator.xor,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}

def evaluate_expression(user_input):
    node = ast.parse(user_input, mode='eval')

    def _evaluate(node):
        if isinstance(node, ast.Expression):
            return _evaluate(node.body)
        elif isinstance(node, ast.Num):  # For Python >= 3.8, use ast.Constant
            return node.n
        elif isinstance(node, ast.BinOp):
            left = _evaluate(node.left)
            right = _evaluate(node.right)
            operator_func = SAFE_OPERATORS[type(node.op)]
            return operator_func(left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = _evaluate(node.operand)
            operator_func = SAFE_OPERATORS[type(node.op)]
            return operator_func(operand)
        else:
            raise TypeError(f"Unsupported type: {type(node).__name__}")

    return _evaluate(node.body)


1. **AST Parsing**: We use `ast.parse` to parse the input string into an AST while specifying `mode='eval'` to ensure it is an expression.
2. **AST Evaluation**: We recursively evaluate the AST nodes, only allowing operations defined in `SAFE_OPERATORS`, which includes basic arithmetic operations.
3. **Security**: By only evaluating specific, safe node types (`ast.Expression`, `ast.Num`, `ast.BinOp`, `ast.UnaryOp`), we prevent arbitrary code execution.

This implementation ensures that the function only evaluates mathematical expressions and does not allow for code injection or execution of unintended code.