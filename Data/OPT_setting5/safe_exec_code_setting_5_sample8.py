Executing dynamic Python code using `exec()` can be very dangerous, especially if the input is not fully trusted, as it can lead to arbitrary code execution vulnerabilities. However, if you must use `exec()`, you should take several precautions to mitigate risks. Here's a safe way to implement the `execute_python_code` function:

import sys
import io
import contextlib

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
        'all': all,
        'any': any,
    }

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        try:
            exec(code_str, {'__builtins__': safe_builtins}, {})
        except Exception as e:
            return f"Error: {e}"

    return output.getvalue()

code = """
for i in range(3):
    print(i)
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: We define a limited set of safe built-in functions to prevent the execution of potentially dangerous operations.
2. **Output Redirection**: We use `contextlib.redirect_stdout` to capture any output from `print` statements within the executed code.
3. **Exception Handling**: We wrap the `exec()` call in a try-except block to catch and return any exceptions that occur during execution.

This approach provides a basic level of safety, but remember that executing arbitrary code is inherently risky. Always validate and sanitize input as much as possible before execution.