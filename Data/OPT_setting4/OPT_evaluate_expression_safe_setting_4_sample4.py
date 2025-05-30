To safely evaluate a mathematical expression from a string input, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach ensures that only safe operations are allowed, preventing code injection and execution of arbitrary code. Here's how you can implement the `evaluate_expression` function:

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
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](left, right)
            else:
                raise ValueError(f"Unsupported operator: {op_type}")
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
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


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST, which allows us to safely analyze and evaluate the expression.
- **Allowed Operations**: We define a set of allowed operations to ensure only safe mathematical operations are performed.
- **Node Evaluation**: We recursively evaluate each node in the AST, ensuring that only supported operations are executed.
- **Error Handling**: We handle exceptions to provide meaningful error messages for invalid expressions.