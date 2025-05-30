To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression without executing arbitrary code. This approach prevents code injection by only allowing a subset of Python's syntax that is safe for mathematical operations.

Here's how you can implement the `evaluate_expression` function:

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
        if isinstance(node, ast.Num):  # Handle numbers
            return node.n
        elif isinstance(node, ast.BinOp):  # Handle binary operations
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            if op_type in operators:
                return operators[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):  # Handle unary operations
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


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST, ensuring that only valid Python expressions are considered.
- **Operator Mapping**: We define a dictionary to map AST operator nodes to corresponding Python functions, ensuring only safe operations are allowed.
- **Node Evaluation**: The `eval_node` function recursively evaluates the AST nodes, handling numbers, binary operations, and unary operations.
- **Error Handling**: The function raises a `ValueError` if the input expression is invalid or contains unsupported operations. 

This approach ensures that only mathematical expressions are evaluated, preventing the execution of arbitrary code.