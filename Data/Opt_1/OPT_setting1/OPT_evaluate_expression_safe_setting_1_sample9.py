To safely evaluate mathematical expressions in Python, we can use the `ast` module, which allows us to parse expressions into an abstract syntax tree and then evaluate them using restricted functionality. This method avoids executing arbitrary code and prevents injection attacks. Here's how you can implement the `evaluate_expression` function securely:

import ast
import operator

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}

def evaluate_expression(user_input):
    try:
        parsed_expr = ast.parse(user_input, mode='eval')
    except SyntaxError:
        raise ValueError("Invalid mathematical expression")

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)
        elif isinstance(node, ast.Num):  # For Python 3.8+ use ast.Constant
            return node.n
        elif isinstance(node, ast.BinOp):
            left_val = evaluate(node.left)
            right_val = evaluate(node.right)
            operator_func = ALLOWED_OPERATORS.get(type(node.op))
            if operator_func:
                return operator_func(left_val, right_val)
            else:
                raise ValueError("Unsupported binary operator")
        elif isinstance(node, ast.UnaryOp):
            operand_val = evaluate(node.operand)
            operator_func = ALLOWED_OPERATORS.get(type(node.op))
            if operator_func:
                return operator_func(operand_val)
            else:
                raise ValueError("Unsupported unary operator")
        else:
            raise ValueError("Unsupported expression element")

    return evaluate(parsed_expr.body)

result = evaluate_expression("3 + 2 * (1 - 5) ** 2 / 2")
print(result)  # Output should be a computed value from the expression

**Explanation**:

- **AST Parsing**: The input string is parsed into an AST using `ast.parse`.
- **Node Evaluation**: We recursively evaluate nodes:
  - **`ast.Num`/`ast.Constant`** represent numbers.
  - **`ast.BinOp`** for binary operations use allowed operators.
  - **`ast.UnaryOp`** handle unary operations like negation.
- **Allowed Operations**: The dictionary `ALLOWED_OPERATORS` specifies supported operations to ensure security.
- **Error Handling**: If the expression syntax is invalid, or if any unsupported operation is encountered, a `ValueError` is raised.

This implementation focuses on clear separation of parsing and evaluation stages while ensuring only safe mathematical expressions can be processed.