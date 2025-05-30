To safely evaluate a mathematical expression from a string input, you can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach ensures that only safe operations are performed, preventing code injection and execution of arbitrary code. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

def evaluate_expression(user_input):
    allowed_operators = {
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
            operator_type = type(node.op)
            if operator_type in allowed_operators:
                return allowed_operators[operator_type](left, right)
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> (e.g., -1)
            operand = eval_node(node.operand)
            operator_type = type(node.op)
            if operator_type in allowed_operators:
                return allowed_operators[operator_type](operand)
        raise ValueError("Unsupported expression")

    try:
        parsed_expr = ast.parse(user_input, mode='eval')
        return eval_node(parsed_expr.body)
    except (SyntaxError, ValueError):
        raise ValueError("Invalid expression")


- **AST Parsing**: The `ast.parse` function is used to parse the input string into an AST. The `mode='eval'` ensures that the input is treated as a single expression.
- **Node Evaluation**: The `eval_node` function recursively evaluates the AST nodes. It handles numbers, binary operations, and unary operations.
- **Allowed Operations**: Only a specific set of operations (addition, subtraction, multiplication, division, power, modulus, and unary negation) are allowed. This prevents execution of arbitrary code.
- **Error Handling**: The function raises a `ValueError` if the expression contains unsupported operations or is syntactically incorrect.