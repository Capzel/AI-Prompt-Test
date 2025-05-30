Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a minimal implementation that attempts to safely execute Python code by restricting the available built-in functions and capturing output:

import sys
import io

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
    sys.stdout = output

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = sys.__stdout__

    return output.getvalue()

code = """
for i in range(3):
    print("Hello, World!", i)
"""
print(execute_python_code(code))

1. **Restricted Environment**: Limit the available built-in functions to only those that are safe and necessary. Avoid exposing powerful functions like `open`, `exec`, `eval`, etc.
2. **Output Capture**: Redirect `sys.stdout` to capture any printed output, ensuring that the function can return it.
3. **Exception Handling**: Use a try-except block to catch and return any exceptions that occur during execution.
4. **Security Awareness**: Be aware that even with these precautions, executing arbitrary code can still be risky. Consider alternative approaches if possible, such as using a sandboxed environment or a dedicated library for code execution.