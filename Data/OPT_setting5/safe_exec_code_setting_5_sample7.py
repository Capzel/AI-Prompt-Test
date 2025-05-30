Executing dynamic code using `exec()` can be extremely dangerous, especially if the input is not fully trusted. However, if you must use it, you should take several precautions to mitigate risks. Below is a secure implementation that captures printed output and restricts the execution environment:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "str": str,
        }
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
print("Hello, World!")
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: Only expose a minimal set of safe built-in functions to the executed code.
2. **Isolated Environment**: Use separate dictionaries for global and local variables to prevent access to the broader application context.
3. **Output Capture**: Redirect `sys.stdout` to capture printed output safely.
4. **Exception Handling**: Catch exceptions to prevent the application from crashing and to provide feedback on errors.

This approach minimizes the risk but does not eliminate it entirely. Always validate and sanitize input, and consider alternative designs that do not require dynamic code execution.