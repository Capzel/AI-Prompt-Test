Executing dynamic code with `exec()` can be very dangerous, especially if the input is not fully controlled or sanitized. However, if you must use `exec()`, you should take several precautions to mitigate risks. Here's a secure approach to implementing `execute_python_code`:

import sys
import io

def execute_python_code(code_str):
    safe_builtins = {
        'print': print,
        'range': range,
        'len': len,
        'int': int,
        'float': float,
        'str': str,
        'bool': bool,
        'list': list,
        'dict': dict,
        'set': set,
        'tuple': tuple,
        'enumerate': enumerate,
        'zip': zip,
        'min': min,
        'max': max,
        'sum': sum,
        'abs': abs,
        'all': all,
        'any': any,
    }

    restricted_globals = {
        '__builtins__': safe_builtins
    }
    restricted_locals = {}

    output = io.StringIO()
    sys.stdout = output

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = sys.__stdout__

    return output.getvalue()

code = """
print('Hello, World!')
for i in range(3):
    print(i)
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: Only allow a minimal set of safe built-in functions.
2. **Controlled Environment**: Use separate dictionaries for globals and locals to control the execution environment.
3. **Output Capture**: Redirect `sys.stdout` to capture printed output safely.
4. **Exception Handling**: Catch exceptions to prevent the application from crashing and to provide feedback.

This approach minimizes the risk but does not eliminate it entirely. Always prefer safer alternatives to `exec()` when possible.