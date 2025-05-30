To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach helps prevent code injection by only allowing safe operations and literals. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

def evaluate_expression(user_input):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.BitXor: operator.xor,
        ast.USub: operator.neg
    }

    def eval_node(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            left = eval_node(node.left)
            right = eval_node(node.right)
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            operand = eval_node(node.operand)
            return operators[type(node.op)](operand)
        else:
            raise TypeError("Unsupported operation")

    try:
        node = ast.parse(user_input, mode='eval').body
        return eval_node(node)
    except (TypeError, ValueError, KeyError):
        raise ValueError("Invalid expression")


- **AST Parsing**: We use `ast.parse` to parse the input string into an AST.
- **Node Evaluation**: We recursively evaluate the AST nodes. Only specific node types (`Num`, `BinOp`, `UnaryOp`) are allowed.
- **Operators Dictionary**: We map AST operator nodes to corresponding Python functions.
- **Error Handling**: We handle potential errors by catching exceptions and raising a `ValueError` for invalid expressions.

This approach ensures that only safe mathematical operations are evaluated, preventing arbitrary code execution.