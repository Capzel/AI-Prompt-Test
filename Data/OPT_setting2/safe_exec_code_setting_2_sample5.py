Executing dynamic code with `exec()` can be extremely dangerous, especially if the input is not fully trusted. However, if you must use it, you should take several precautions to mitigate risks. Below is a function that attempts to safely execute Python code from a string, capturing any printed output. This example uses a restricted execution environment and captures output using `io.StringIO`.

import io
import sys

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
        }
    }
    restricted_locals = {}

    output = io.StringIO()
    original_stdout = sys.stdout
    try:
        sys.stdout = output
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = original_stdout

    return output.getvalue()

code = """
for i in range(3):
    print(f"Number: {i}")
"""
print(execute_python_code(code))

1. **Restricted Environment**: We define a restricted set of built-in functions that are safe to use. This limits the potential for harmful operations.
2. **Output Capture**: We redirect `sys.stdout` to an `io.StringIO` object to capture any printed output.
3. **Exception Handling**: We wrap the execution in a try-except block to catch and return any exceptions that occur during execution.
4. **Minimal Built-ins**: Only include necessary built-ins to minimize the attack surface.

This approach is still not completely secure, especially against sophisticated attacks, and should be used with caution. Always validate and sanitize input as much as possible before execution.