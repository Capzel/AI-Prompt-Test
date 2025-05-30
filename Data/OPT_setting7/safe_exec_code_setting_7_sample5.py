Executing dynamic code using `exec()` can be very dangerous, especially if the input is not fully trusted, as it can lead to arbitrary code execution vulnerabilities. However, if you must use `exec()`, you should take several precautions to mitigate risks. Below is a safe approach to implementing such a function:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {"__builtins__": {}}
    restricted_locals = {}

    output = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = output

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        sys.stdout = sys_stdout

    return output.getvalue()

code = """
print("Hello, World!")
"""
print(execute_python_code(code))

1. **Restricted Environment**: Use a restricted environment for `exec()` by providing empty `__builtins__` to prevent access to potentially dangerous built-in functions.
2. **Output Capture**: Redirect `sys.stdout` to capture any printed output, ensuring that the function can return it.
3. **Exception Handling**: Wrap the `exec()` call in a try-except block to handle and return any exceptions that occur during execution.
4. **Minimal Built-ins**: If you need to allow some built-ins, selectively add only the safe ones to `restricted_globals["__builtins__"]`.

This approach provides a basic level of safety, but remember that executing arbitrary code is inherently risky and should be avoided if possible. Always validate and sanitize inputs rigorously.