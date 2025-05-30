To safely evaluate a mathematical expression provided as a string, we can use Python's Abstract Syntax Trees (AST) module to parse and evaluate the expression. By specifically allowing only safe nodes, we prevent any potentially malicious code from being executed. Here’s how you can implement it:

import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg
}

def evaluate_expression(user_input):
    """
    Safely evaluate a mathematical expression from a string.
    
    :param user_input: A string containing the math expression.
    :return: The result of the expression as a number.
    :raises: ValueError if the expression contains disallowed elements.
    """
    
    def _evaluate(node):
        if isinstance(node, ast.Num):  # Python 3.7 and earlier
            return node.n
        elif hasattr(ast, 'Constant') and isinstance(node, ast.Constant):  # Python 3.8+
            return node.value
        elif isinstance(node, ast.BinOp):
            left = _evaluate(node.left)
            right = _evaluate(node.right)
            operator_func = OPERATORS[type(node.op)]
            return operator_func(left, right)
        elif isinstance(node, ast.UnaryOp):
            operand = _evaluate(node.operand)
            operator_func = OPERATORS[type(node.op)]
            return operator_func(operand)
        else:
            raise ValueError("Unsupported expression")

    try:
        tree = ast.parse(user_input, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid syntax")
    
    return _evaluate(tree.body)



1. **AST Parsing**: By using `ast.parse()`, we convert the input string to an Abstract Syntax Tree, which helps us navigate structured parts of the input.

2. **Safe Evaluation**: We evaluate only specific nodes (`Num`, `BinOp`, `UnaryOp`) and use operator mappings to handle operations securely.

3. **Restricting Nodes**: By limiting the nodes we evaluate and the operations permitted, we prevent execution of arbitrary or harmful code.

4. **Error Handling**: Proper error handling provides user-friendly and secure explanations for invalid inputs or operations.

This approach ensures that only mathematical expressions are evaluated, guarding against potential security risks arising from inputs with malicious intent.