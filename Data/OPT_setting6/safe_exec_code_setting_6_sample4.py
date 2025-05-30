Using `exec()` to execute dynamically generated Python code poses significant security risks, especially if the input comes from an untrusted source. However, for educational purposes, here’s an example of how to implement `execute_python_code` with some precautions:

import sys
import io

def execute_python_code(code_str):
    safe_builtins = {
        'print': print,
        'range': range,
        'len': len,
        'int': int,
        'str': str,
        'float': float,
        'bool': bool,
        'list': list,
        'dict': dict,
    }

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    safe_globals = {
        '__builtins__': safe_builtins
    }
    safe_locals = {}

    try:
        exec(code_str, safe_globals, safe_locals)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {str(e)}"
    finally:
        sys.stdout = old_stdout

    return output

code = """
print("Hello, World!")
x = 5
print(x + 10)
"""
output = execute_python_code(code)
print("Captured Output:", output)

1. **Restricted Built-ins**: Limit the available built-in functions to a safe subset to prevent potentially harmful operations.
2. **Sandboxed Execution**: Use separate `safe_globals` and `safe_locals` dictionaries to minimize the risk of code affecting the broader environment.
3. **Output Capture**: Redirect `sys.stdout` to capture any output from `print` statements.
4. **Exception Handling**: Wrap execution in a `try-except` block to handle and report errors gracefully.

**Caution**: Even with these measures, executing arbitrary code strings can still be risky. This example is for educational purposes, and using `exec()` is generally discouraged in production environments unless absolutely necessary and properly sandboxed.