To safely evaluate a mathematical expression from a string, we can use the Abstract Syntax Trees (AST) module in Python. This approach ensures that the input is parsed as a mathematical expression and not as arbitrary executable code, which helps prevent code injection vulnerabilities.

Here is a secure implementation:

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
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g. -1
            operand = eval_node(node.operand)
            return operators[type(node.op)](operand)
        else:
            raise TypeError("Unsupported expression")

    try:
        node = ast.parse(user_input, mode='eval').body
        return eval_node(node)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

result = evaluate_expression("2 + 3 * (4 - 1) / 2 ** 2")
print(result)  # Output: 3.25


- **AST Module**: We use the `ast.parse()` method to parse the input string into an abstract syntax tree. We only allow expressions by specifying `mode='eval'`.
- **Operators**: We define a mapping between AST operator nodes and Python's operator functions, supporting basic arithmetic operations.
- **Recursive Evaluation**: The `eval_node` function recursively evaluates the AST nodes, handling numbers, binary operations, and unary operations.
- **Error Handling**: We catch exceptions that may arise during parsing or evaluation and raise a `ValueError` with an appropriate message for invalid expressions.

This implementation is secure against code injection and only evaluates valid mathematical expressions.