import ast
import operator

def evaluate_expression(user_input):
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.BitXor: operator.xor,
        ast.USub: operator.neg
    }

    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
            left = eval_node(node.left)
            right = eval_node(node.right)
            return allowed_operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp) and type(node.op) in allowed_operators:
            operand = eval_node(node.operand)
            return allowed_operators[type(node.op)](operand)
        else:
            raise ValueError("Unsupported operation")

    try:
        tree = ast.parse(user_input, mode='eval')
        return eval_node(tree.body)
    except Exception:
        raise ValueError("Invalid expression")