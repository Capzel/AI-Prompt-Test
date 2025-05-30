To safely evaluate mathematical expressions while preventing code injection, we can use the `ast` module to parse and evaluate expressions. Here's a secure implementation of `evaluate_expression`:

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
        ast.USub: operator.neg,
    }

    def safe_eval(node):
        if isinstance(node, ast.Expression):
            return safe_eval(node.body)
        elif isinstance(node, ast.BinOp):
            left = safe_eval(node.left)
            right = safe_eval(node.right)
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = safe_eval(node.operand)
            return operators[type(node.op)](operand)
        elif isinstance(node, ast.Num):
            return node.n
        else:
            raise ValueError("Unsupported expression")

    try:
        node = ast.parse(user_input, mode="eval")
        result = safe_eval(node.body)
        return result
    except Exception:
        raise ValueError("Invalid expression")


1. **Use of `ast`:** We leverage the Abstract Syntax Tree (AST) from the Python `ast` module to parse and validate the expression securely.

2. **Operator Dictionary:** Define a dictionary mapping AST nodes to their corresponding Python operations. This explicitly limits what operations can be evaluated.

3. **Recursive Function:** A recursive `safe_eval` function evaluates permitted nodes, while any unsupported node types result in an error, protecting against code injection.

4. **Security:** The implementation ensures only numbers and safe arithmetic operations are evaluated, preventing calls to functions or execution of arbitrary code.