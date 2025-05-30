To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach ensures that only safe operations are performed, preventing code injection and execution of arbitrary code. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

def evaluate_expression(user_input):
    operators = {
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
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            left = eval_node(node.left)
            right = eval_node(node.right)
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            operand = eval_node(node.operand)
            return operators[type(node.op)](operand)
        else:
            raise TypeError("Unsupported operation")

    try:
        node = ast.parse(user_input, mode='eval').body
        return eval_node(node)
    except (TypeError, KeyError, ZeroDivisionError) as e:
        raise ValueError("Invalid expression") from e


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST, which allows us to safely evaluate the expression.
- **Operator Mapping**: We define a dictionary to map AST operator nodes to their corresponding Python functions.
- **Node Evaluation**: We recursively evaluate each node in the AST, ensuring only safe operations are performed.
- **Error Handling**: We handle potential errors such as unsupported operations and division by zero, raising a `ValueError` for invalid expressions.