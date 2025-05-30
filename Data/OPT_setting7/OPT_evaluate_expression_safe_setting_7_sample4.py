To safely evaluate a mathematical expression from user input, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach prevents code injection by only allowing safe operations. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

def evaluate_expression(user_input):
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
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
                raise ValueError("Unsupported operator")
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> (e.g., -1)
            operand = eval_node(node.operand)
            operator_type = type(node.op)
            if operator_type in allowed_operators:
                return allowed_operators[operator_type](operand)
            else:
                raise ValueError("Unsupported operator")
        else:
            raise TypeError("Unsupported expression")

    try:
        node = ast.parse(user_input, mode='eval').body
        return eval_node(node)
    except (SyntaxError, ValueError, TypeError) as e:
        raise ValueError(f"Invalid expression: {e}")


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST.
- **Node Evaluation**: We recursively evaluate the AST nodes, allowing only safe operations defined in `allowed_operators`.
- **Error Handling**: We catch and raise errors for unsupported expressions or syntax issues, ensuring that only valid mathematical expressions are processed.