To securely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) to parse and evaluate the expression. This approach mitigates the risk of code injection by restricting the allowed operations to a safe subset of Python's expression capabilities. Here's how you can implement it:

import ast
import operator

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.BitXor: operator.xor,
    ast.USub: operator.neg
}

def evaluate_expression(user_input):
    """
    Safely evaluate a mathematical expression passed as a string.
    
    Parameters:
    - user_input (str): The mathematical expression to evaluate.
    
    Returns:
    - float: The result of the evaluated expression.
    
    Raises:
    - ValueError: If the expression contains unsafe or unsupported operations.
    """
    try:
        node = ast.parse(user_input, mode='eval').body
        return _evaluate_ast_node(node)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

def _evaluate_ast_node(node):
    """Recursively evaluate an AST node."""
    if isinstance(node, ast.Num):  # For Python 3.7 and earlier
        return node.n
    elif isinstance(node, ast.Constant):  # For Python 3.8 and later
        return node.value
    elif isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
        left = _evaluate_ast_node(node.left)
        right = _evaluate_ast_node(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_OPERATORS:
        operand = _evaluate_ast_node(node.operand)
        return ALLOWED_OPERATORS[type(node.op)](operand)
    else:
        raise ValueError("Unsupported operation")


- **AST Parsing**: We parse the input string into an AST. The `ast.parse` function generates an AST from the input string in `eval` mode, which is suitable for evaluating expressions.
- **Node Evaluation**: We recursively evaluate the AST nodes. Only specific node types (`Num`, `Constant`, `BinOp`, `UnaryOp`) and operators defined in `ALLOWED_OPERATORS` are supported.
- **Security**: This method prevents arbitrary code execution by limiting the parsed and evaluated nodes to a predefined set of safe operations.