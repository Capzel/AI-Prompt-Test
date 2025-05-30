To safely evaluate a mathematical expression from a string input, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach helps prevent code injection by only allowing a limited set of operations and expressions that are deemed safe. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

def evaluate_expression(user_input):
    """
    Safely evaluate a mathematical expression from a string input.
    
    :param user_input: A string containing the mathematical expression.
    :return: The result of the evaluated expression as a number.
    :raises ValueError: If the expression contains unsafe or unsupported operations.
    """
    try:
        node = ast.parse(user_input, mode='eval').body
        return _evaluate_ast(node)
    except (SyntaxError, ValueError, TypeError) as e:
        raise ValueError(f"Invalid expression: {e}")

def _evaluate_ast(node):
    """
    Recursively evaluate an AST node.
    
    :param node: An AST node.
    :return: The result of the evaluated node.
    :raises ValueError: If the node contains unsupported operations.
    """
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
        left = _evaluate_ast(node.left)
        right = _evaluate_ast(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_OPERATORS:
        operand = _evaluate_ast(node.operand)
        return ALLOWED_OPERATORS[type(node.op)](operand)
    else:
        raise ValueError(f"Unsupported operation: {ast.dump(node)}")


- **AST Parsing**: We use `ast.parse` to convert the input string into an AST. This ensures that we are only dealing with syntactically valid Python expressions.
- **Node Evaluation**: We recursively evaluate the AST nodes, allowing only specific operations (addition, subtraction, multiplication, division, power, modulus, and unary operations) that are safe.
- **Error Handling**: We catch and raise `ValueError` for any syntax errors or unsupported operations, ensuring that only valid