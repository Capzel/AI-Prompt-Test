To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression without executing arbitrary code. Here's a secure implementation using the `ast` module:

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
        ast.USub: operator.neg,
    }
    
    def evaluate_node(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            left = evaluate_node(node.left)
            right = evaluate_node(node.right)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](left, right)
            else:
                raise ValueError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            operand = evaluate_node(node.operand)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](operand)
            else:
                raise ValueError(f"Unsupported operator: {op_type}")
        else:
            raise TypeError(f"Unsupported type: {type(node)}")

    try:
        parsed_expr = ast.parse(user_input, mode='eval')
        return evaluate_node(parsed_expr.body)
    except (SyntaxError, ValueError, TypeError) as e:
        raise ValueError(f"Invalid expression: {e}")

result = evaluate_expression("2 + 3 * (4 - 1) ** 2")
print(result)  # Output: 29

1. **Allowed Operators**: We define a dictionary of allowed operators, mapping AST nodes to Python's operator functions.
2. **Node Evaluation**: We recursively evaluate each node in the AST:
   - **Numbers**: Directly return the number.
   - **Binary Operations**: Recursively evaluate left and right nodes and apply the operator.
   - **Unary Operations**: Evaluate the operand and apply the unary operator.
3. **Error Handling**: We handle syntax, type, and value errors gracefully, raising a `ValueError` if the expression is invalid or contains unsupported operations.