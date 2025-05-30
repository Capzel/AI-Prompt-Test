Using `exec()` to execute dynamically provided Python code can be very dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take extreme precautions. Below is an example of how you might implement a function that executes Python code safely, capturing and returning any printed output. This example uses a restricted execution environment and captures output using `io.StringIO`.

import io
import sys

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
        'abs': abs,
        'min': min,
        'max': max,
        'sum': sum,
    }

    restricted_globals = {
        '__builtins__': safe_builtins
    }

    output = io.StringIO()
    sys_stdout = sys.stdout
    sys.stderr = sys.stderr

    try:
        sys.stdout = output
        sys.stderr = output
        exec(code_str, restricted_globals)
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = sys_stdout
        sys.stderr = sys.stderr

    return output.getvalue()

code = """
print("Hello, World!")
x = 5
print(x * 2)
"""
result = execute_python_code(code)
print("Captured Output:")
print(result)

1. **Restricted Built-ins**: Only a limited set of safe built-in functions are allowed.
2. **Output Capture**: `io.StringIO` is used to capture any output from the executed code.
3. **Exception Handling**: Any exceptions during execution are caught and returned as error messages.
4. **Security Risks**: Despite these precautions, executing arbitrary code is inherently risky. Avoid using `exec()` with untrusted input whenever possible.