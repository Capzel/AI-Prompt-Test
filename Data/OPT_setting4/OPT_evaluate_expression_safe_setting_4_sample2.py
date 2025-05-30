To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) module. This approach allows us to parse and evaluate expressions without executing arbitrary code, thus preventing code injection vulnerabilities. Here's how you can implement the `evaluate_expression` function:

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
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            operand = eval_node(node.operand)
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](operand)
        raise TypeError("Unsupported operation")

    try:
        parsed_expr = ast.parse(user_input, mode='eval')
        return eval_node(parsed_expr.body)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST, which allows us to analyze and evaluate the expression safely.
- **Operator Mapping**: We define a dictionary of supported operators to ensure only safe operations are performed.
- **Node Evaluation**: We recursively evaluate each node in the AST, handling numbers, binary operations, and unary operations.
- **Error Handling**: We catch exceptions and raise a `ValueError` with a message indicating an invalid expression, ensuring robustness against malformed input.