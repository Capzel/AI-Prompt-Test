Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a secure implementation that captures printed output and restricts the execution environment:

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
        return f"Error: {str(e)}"
    finally:
        sys.stdout = sys.__stdout__

    return output.getvalue()

code = """
print("Hello, World!")
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: Only expose a minimal set of safe built-in functions to the executed code.
2. **Exception Handling**: Capture and return any exceptions to prevent the application from crashing.
3. **Output Redirection**: Redirect `sys.stdout` to capture printed output, ensuring it can be returned or logged securely.
4. **Environment Isolation**: Use separate `globals` and `locals` dictionaries to isolate the execution environment.

Despite these precautions, using `exec()` is inherently risky, and it's generally advisable to avoid executing untrusted code whenever possible.