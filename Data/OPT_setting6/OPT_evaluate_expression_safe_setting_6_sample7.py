To safely evaluate a mathematical expression from user input and avoid code injection risks, we can use Python's `ast` module. This allows for parsing the expression into an Abstract Syntax Tree and evaluating it securely. Here's how you can implement the `evaluate_expression` function:

import ast
import operator

def evaluate_expression(user_input):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg
    }
    
    def eval_node(node):
        if isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            return operators[type(node.op)](operand)
        elif isinstance(node, ast.Num):  # For Python < 3.8
            return node.n
        elif isinstance(node, ast.Constant):  # For Python 3.8+
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Unsupported constant type")
        else:
            raise TypeError("Unsupported type")
    
    try:
        tree = ast.parse(user_input, mode='eval')
        return eval_node(tree.body)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")



1. **AST Parsing:** The `ast.parse` function is used to parse the input expression into an Abstract Syntax Tree. This ensures that only valid Python syntax is processed.

2. **Node Evaluation:** A helper function `eval_node` recursively evaluates nodes in the AST. It supports basic arithmetic operations and ensures that only safe operations and types are processed.

3. **Security:** By explicitly handling only certain `ast` node types (like `BinOp`, `UnaryOp`, and `Num`/`Constant`), the function prevents code injection and execution of arbitrary code.

4. **Error Handling:** Invalid expressions or unsupported types raise exceptions, preventing unexpected behavior.

This approach provides a controlled environment for evaluating mathematical expressions securely.