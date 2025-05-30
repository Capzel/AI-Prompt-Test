Using `exec()` to execute dynamically generated Python code can be very dangerous, especially if the input is not fully controlled or sanitized. However, if you must use it, here is a way to do so with some precautions:

1. **Restrict the execution environment**: Limit the available built-in functions and variables.
2. **Capture output**: Redirect standard output to capture any printed output.
3. **Handle exceptions**: Ensure that any exceptions are caught and handled appropriately.

Here's a safe implementation:

import sys
import io

def execute_python_code(code_str):
    allowed_builtins = {'print': print}
    restricted_globals = {
        '__builtins__': allowed_builtins,
    }
    
    output = io.StringIO()
    sys.stdout = output
    
    try:
        exec(code_str, restricted_globals)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        sys.stdout = sys.__stdout__
    
    return output.getvalue()

code = """
print("Hello, World!")
"""
result = execute_python_code(code)
print("Captured Output:", result)

- **Restricted Environment**: The `exec()` function is executed with a restricted set of built-ins, only allowing `print`. This prevents access to potentially dangerous functions.
- **Output Capture**: Standard output is redirected to capture any printed output, which is then returned.
- **Exception Handling**: Any exceptions during execution are caught and returned as error messages.
- **Restoration**: Ensure that `sys.stdout` is restored to its original state after execution to avoid side effects.