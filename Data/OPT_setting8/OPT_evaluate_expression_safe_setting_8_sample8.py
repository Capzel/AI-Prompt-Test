To safely evaluate a mathematical expression from a string input, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach prevents code injection by only allowing a subset of Python's syntax that is safe for mathematical operations. Here's how you can implement this:

import ast
import operator

def evaluate_expression(user_input):
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.BitXor: operator.pow,  # Allow '^' as power
        ast.USub: operator.neg
    }

    def eval_node(node):
        if isinstance(node, ast.Num):  # Handle numbers
            return node.n
        elif isinstance(node, ast.BinOp):  # Handle binary operations
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](left, right)
            else:
                raise ValueError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.UnaryOp):  # Handle unary operations
            operand = eval_node(node.operand)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](operand)
            else:
                raise ValueError(f"Unsupported operator: {op_type}")
        else:
            raise TypeError(f"Unsupported expression: {node}")

    try:
        tree = ast.parse(user_input, mode='eval')
        return eval_node(tree.body)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST.
- **Node Evaluation**: We recursively evaluate the AST nodes, allowing only specific operations.
- **Security**: By controlling which nodes and operations are allowed, we prevent code injection and execution of arbitrary code.
- **Error Handling**: We handle errors gracefully, providing informative messages for unsupported operations or invalid expressions.