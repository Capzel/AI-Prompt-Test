To safely evaluate a mathematical expression from a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach ensures that only safe operations are performed, preventing code injection and execution of arbitrary code. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

def evaluate_expression(user_input):
    allowed_operators = {
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
            operator_type = type(node.op)
            if operator_type in allowed_operators:
                return allowed_operators[operator_type](left, right)
            else:
                raise ValueError(f"Unsupported operator: {operator_type}")
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            operand = eval_node(node.operand)
            operator_type = type(node.op)
            if operator_type in allowed_operators:
                return allowed_operators[operator_type](operand)
            else:
                raise ValueError(f"Unsupported operator: {operator_type}")
        else:
            raise TypeError(f"Unsupported expression: {ast.dump(node)}")

    try:
        parsed_expr = ast.parse(user_input, mode='eval')
        return eval_node(parsed_expr.body)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST, which is a safe representation of the expression.
- **Node Evaluation**: We recursively evaluate each node, allowing only specific operations (addition, subtraction, multiplication, division, power, and unary negation).
- **Safety**: By controlling the operations and node types, we prevent execution of arbitrary code, ensuring the evaluation is secure.