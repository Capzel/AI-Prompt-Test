import sys
import io

def execute_python_code(code_str):
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        exec(code_str, {})
        output = sys.stdout.getvalue()
    except Exception as e:
        output = str(e)
    finally:
        sys.stdout = original_stdout
    return output