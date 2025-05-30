Below is a function that securely evaluates a mathematical expression provided as a string by using Python's `ast` module. This approach parses the expression into an abstract syntax tree and ensures only safe operations and functions are executed, preventing code injection and other security risks.

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
        if isinstance(node, ast.Num):  # Directly return number nodes
            return node.n
        elif isinstance(node, ast.BinOp):  # Binary operations like addition, multiplication
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](left, right)
            else:
                raise ValueError("Unsupported operation")
        elif isinstance(node, ast.UnaryOp):  # Negative numbers
            operand = eval_node(node.operand)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](operand)
            else:
                raise ValueError("Unsupported operation")
        else:
            raise ValueError("Unsupported syntax")
    
    try:
        parsed_ast = ast.parse(user_input, mode='eval')  # Parse expression
        return eval_node(parsed_ast.body)  # Evaluate the body of the expression
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")

try:
    result = evaluate_expression("2 + 3 * (4 - 1)")
    print(f"Result: {result}")
except ValueError as e:
    print(e)

- **AST Module**: Uses the `ast` module to safely parse and evaluate expressions, thereby preventing code execution.
- **Allowed Operators**: Explicitly checks and supports a limited set of safe operations.
- **Error Handling**: Gracefully handles errors and unsupported syntax ensuring that the function does not execute unsafe or unexpected code.
- **Security**: Mitigates risks from arbitrary code execution by not using `eval` directly.