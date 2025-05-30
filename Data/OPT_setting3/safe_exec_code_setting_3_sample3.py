Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a secure implementation that uses `exec()` with some safety measures:

import sys
import io
import contextlib

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
        'set': set,
        'tuple': tuple,
    }

    restricted_globals = {
        '__builtins__': safe_builtins
    }
    restricted_locals = {}

    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        try:
            exec(code_str, restricted_globals, restricted_locals)
        except Exception as e:
            return f"Error: {e}"

    return output.getvalue()

code = """
print("Hello, World!")
for i in range(3):
    print(i)
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: Only a limited set of safe built-in functions are allowed. This prevents the execution of potentially dangerous functions.
2. **Controlled Environment**: The `exec()` function is executed with restricted global and local dictionaries to limit the scope of what the executed code can access.
3. **Output Capture**: The `contextlib.redirect_stdout` is used to capture any output from the executed code, which is then returned.

Despite these precautions, using `exec()` is inherently risky, and it's generally better to avoid executing arbitrary code strings whenever possible. Consider alternative designs that do not require dynamic code execution.