To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach prevents code injection by ensuring that only safe operations are performed. Here's how you can implement the `evaluate_expression` function:

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
            raise TypeError(f"Unsupported operation: {ast.dump(node)}")

    try:
        node = ast.parse(user_input, mode='eval').body
        return eval_node(node)
    except (TypeError, KeyError, ZeroDivisionError) as e:
        raise ValueError(f"Invalid expression: {e}")


- **AST Parsing**: We use `ast.parse` to parse the input string into an AST.
- **Node Evaluation**: We recursively evaluate the AST nodes. Only nodes representing numbers, binary operations, and unary operations are supported.
- **Operators**: We map AST operator nodes to corresponding Python functions using the `operator` module.
- **Error Handling**: We catch and raise errors for unsupported operations, key errors, and division by zero to ensure the function only evaluates valid mathematical expressions.