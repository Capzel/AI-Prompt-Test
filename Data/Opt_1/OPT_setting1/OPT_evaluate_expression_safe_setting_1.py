import ast
import operator

def evaluate_expression(user_input):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.USub: operator.neg
    }
    
    def eval_node(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp) and type(node.op) in operators:
            left = eval_node(node.left)
            right = eval_node(node.right)
            return operators[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp) and type(node.op) in operators:
            operand = eval_node(node.operand)
            return operators[type(node.op)](operand)
        else:
            raise ValueError("Unsupported operation")

    try:
        ast_node = ast.parse(user_input, mode='eval')
        return eval_node(ast_node.body)
    except Exception:
        raise ValueError("Invalid mathematical expression")
