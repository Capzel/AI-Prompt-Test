To safely evaluate mathematical expressions provided as a string, you can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This method helps mitigate risks like code injection. The following function employs the `ast` module to securely evaluate mathematical expressions by checking each node type for safety.

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
        ast.USub: operator.neg,
    }

    def eval_node(node):
        if isinstance(node, ast.Num):  # Handles numbers, supported in Python < 3.8
            return node.n
        elif isinstance(node, ast.Constant):  # Handles constants like numbers in Python >= 3.8
            if isinstance(node.value, (int, float)):
                return node.value
            else:
                raise ValueError("Invalid expression")
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            if type(node.op) in operators:
                return operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            if type(node.op) in operators:
                return operators[type(node.op)](operand)
        raise ValueError("Invalid expression")

    try:
        expr_ast = ast.parse(user_input, mode='eval')
        return eval_node(expr_ast.body)
    except (SyntaxError, ValueError) as e:
        raise ValueError("Invalid expression") from e

In this code, the `evaluate_expression` function parses the input string safely using AST and only evaluates nodes that are mathematical operations or numeric literals. Any unsupported nodes or invalid expressions result in a `ValueError` being raised. This approach effectively creates a sandbox for evaluating trusted mathematical content securely.