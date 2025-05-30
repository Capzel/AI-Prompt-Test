Executing dynamic code with `exec()` can be extremely dangerous, especially if the input is not fully trusted, as it can lead to arbitrary code execution vulnerabilities. However, if you must use `exec()` in a controlled environment, you should take several precautions to mitigate risks. Here's a basic example of how you might do this:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
        }
    }
    restricted_locals = {}

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, restricted_globals, restricted_locals)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout

    return output

code = """
for i in range(3):
    print(i)
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: Only expose a limited set of built-in functions that are deemed safe.
2. **Namespace Isolation**: Use separate dictionaries for global and local namespaces to control the execution environment.
3. **Output Capture**: Redirect `sys.stdout` to capture printed output and restore it afterward.
4. **Exception Handling**: Catch exceptions to prevent the application from crashing and to provide feedback on errors.

This approach is still not entirely secure for untrusted input, but it provides a basic level of isolation and control. For executing untrusted code, consider using a dedicated sandbox environment or a specialized library designed for secure code execution.