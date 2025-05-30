Executing dynamically provided Python code using `exec()` can be inherently dangerous due to the potential for arbitrary code execution, which could lead to security vulnerabilities. However, if you must use `exec()`, you should take strong precautions. Here's a more secure way to handle this task:

1. Restrict the execution environment.
2. Capture output safely.
3. Handle exceptions gracefully.

Here's an implementation:

import sys
import contextlib
import io

def execute_python_code(code_str):
    allowed_builtins = {'print': print}
    safe_locals = {}

    output_buffer = io.StringIO()

    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code_str, {'__builtins__': allowed_builtins}, safe_locals)
    except Exception as e:
        return f"Error: {e}"

    return output_buffer.getvalue()

code = """
print('Hello, world!')
"""
output = execute_python_code(code)
print(output)


- **Restricted Built-ins**: We limit the built-ins to only what's necessary (`print` in this case), to prevent the executed code from performing unsafe operations.
- **Controlled Environment**: By providing empty `safe_locals`, we restrict access to the global and local namespaces.
- **Output Capture**: We use `io.StringIO()` and `contextlib.redirect_stdout()` to safely capture and return any printed output.
- **Exception Handling**: We catch exceptions to prevent the application from crashing and return error messages safely. 

This implementation should be used with caution, and only in scenarios where executing dynamic code is absolutely necessary and trusted inputs are assured.