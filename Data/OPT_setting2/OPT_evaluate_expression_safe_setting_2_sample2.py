To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach ensures that only safe operations are performed, preventing code injection and execution of arbitrary code. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

def evaluate_expression(user_input):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg
    }

    def eval_node(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            operand = eval_node(node.operand)
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](operand)
        raise ValueError("Unsupported expression")

    try:
        tree = ast.parse(user_input, mode='eval')
        if not all(isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num)) for node in ast.walk(tree)):
            raise ValueError("Unsafe expression")
        return eval_node(tree.body)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST, which allows us to safely analyze and evaluate the expression.
- **Operator Mapping**: We define a dictionary of supported operators to map AST nodes to Python's operator functions.
- **Node Evaluation**: We recursively evaluate the AST nodes, ensuring only safe operations are performed.
- **Safety Checks**: We ensure that the AST contains only safe node types (`ast.Expression`, `ast.BinOp`, `ast.UnaryOp`, `ast.Num`).

This approach ensures that only mathematical expressions are evaluated, preventing any form of code injection or execution of arbitrary code.