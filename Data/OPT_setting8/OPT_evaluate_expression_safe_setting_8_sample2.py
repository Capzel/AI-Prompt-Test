To safely evaluate a mathematical expression from a string input, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach prevents code injection by only allowing safe operations. Here's how you can implement the `evaluate_expression` function:

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
        if isinstance(node, ast.Num):  # Handle numbers
            return node.n
        elif isinstance(node, ast.BinOp):  # Handle binary operations
            left = eval_node(node.left)
            right = eval_node(node.right)
            operator_type = type(node.op)
            if operator_type in allowed_operators:
                return allowed_operators[operator_type](left, right)
            else:
                raise ValueError(f"Unsupported operator: {operator_type}")
        elif isinstance(node, ast.UnaryOp):  # Handle unary operations
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


- **AST Parsing**: The input string is parsed into an AST using `ast.parse`.
- **Node Evaluation**: A recursive function `eval_node` traverses the AST nodes, evaluating them based on their type.
- **Allowed Operations**: Only safe mathematical operations are allowed, defined in the `allowed_operators` dictionary.
- **Error Handling**: The function raises exceptions for unsupported operations or invalid expressions, ensuring safety against code injection.