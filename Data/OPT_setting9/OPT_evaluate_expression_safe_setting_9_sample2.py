To safely evaluate a mathematical expression from a string input, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach helps prevent code injection by only allowing a subset of safe operations. Here's how you can implement the `evaluate_expression` function:

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
        ast.UAdd: operator.pos,
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
                raise ValueError("Unsupported operation")
        elif isinstance(node, ast.UnaryOp):  # Handle unary operations
            operand = eval_node(node.operand)
            operator_type = type(node.op)
            if operator_type in allowed_operators:
                return allowed_operators[operator_type](operand)
            else:
                raise ValueError("Unsupported operation")
        else:
            raise ValueError("Unsupported expression")

    try:
        tree = ast.parse(user_input, mode='eval')
        if not isinstance(tree, ast.Expression):
            raise ValueError("Invalid expression")
        return eval_node(tree.body)
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST.
- **Node Evaluation**: We recursively evaluate the AST nodes, only allowing operations defined in `allowed_operators`.
- **Security**: By restricting the operations to a predefined set, we prevent arbitrary code execution, thus mitigating code injection risks.
- **Error Handling**: We raise a `ValueError` for unsupported operations or invalid expressions to handle errors gracefully.