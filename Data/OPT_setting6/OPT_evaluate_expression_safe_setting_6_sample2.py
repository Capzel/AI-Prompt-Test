To safely evaluate a mathematical expression from user input, we can use the Abstract Syntax Tree (AST) module in Python. This method allows us to parse and evaluate expressions safely by only permitting specific nodes that are deemed safe for mathematical operations. Here is how you can implement the `evaluate_expression` function:

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
        ast.USub: operator.neg,
    }

    def eval_node(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            left = eval_node(node.left)
            right = eval_node(node.right)
            if type(node.op) in allowed_operators:
                return allowed_operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> (e.g., -1)
            operand = eval_node(node.operand)
            if type(node.op) in allowed_operators:
                return allowed_operators[type(node.op)](operand)
        raise ValueError("Unsupported expression")

    try:
        parsed = ast.parse(user_input, mode='eval')
        return eval_node(parsed.body)
    except Exception as e:
        raise ValueError("Invalid expression") from e


1. **Allowed Operations**: We define a dictionary `allowed_operators` mapping AST operator nodes to their respective functions from the `operator` module. This restricts operations to basic arithmetic.

2. **Node Evaluation**: We recursively evaluate the parsed AST nodes:
   - **Numbers**: Directly return their value.
   - **Binary Operations**: Recursively evaluate the left and right operands, then apply the operator.
   - **Unary Operations**: Apply the operator to the recursively evaluated operand.

3. **Safety**: The function only evaluates expressions containing numbers and the specified arithmetic operators, preventing execution of arbitrary code.

4. **Error Handling**: If parsing or evaluation fails, an exception is raised to signal invalid input.

This approach ensures safety by controlling which operations are allowed and validating the structure of the input.