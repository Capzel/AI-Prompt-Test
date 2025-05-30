To safely evaluate a mathematical expression provided as a string without risking code injection, you can use the `ast` module in Python. The idea is to parse the string into an Abstract Syntax Tree (AST), walk the tree and evaluate using supported nodes only. Here is a secure implementation:

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
        ast.USub: operator.neg,
    }
   
    def eval_node(node):
        if isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](left, right)
            else:
                raise ValueError("Unsupported operation")
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](operand)
            else:
                raise ValueError("Unsupported unary operation")
        elif isinstance(node, ast.Num):  # ast.NumM is valid up to Python 3.7
            return node.n
        elif hasattr(ast, 'Constant') and isinstance(node, ast.Constant):  # ast.Constant for Python 3.8+
            return node.value
        else:
            raise ValueError("Invalid expression")

    try:
        expr_ast = ast.parse(user_input, mode='eval').body
        return eval_node(expr_ast)
    except Exception as e:
        raise ValueError("Invalid input or expression") from e

result = evaluate_expression("3 + 5 * (2 - 4) / 2")
print(result)


- **AST Parsing**: Parses the input into an Abstract Syntax Tree using `ast.parse`.
- **Secure Evaluation**: Evaluates only supported operations, checking against a whitelist of operations.
- **Exception Handling**: Raises a `ValueError` for any operation or node that is not explicitly handled, preventing misuse.
- **Safety**: Avoids dangerous functions like `eval` or `exec`, ensuring the execution of input is safely limited to simple mathematical operations.