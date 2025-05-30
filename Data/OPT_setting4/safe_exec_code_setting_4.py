import sys
import io

def execute_python_code(code_str):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    try:
        exec(code_str, {'__builtins__': {}})
    except Exception as e:
        return str(e)
    finally:
        sys.stdout = old_stdout
    return new_stdout.getvalue()