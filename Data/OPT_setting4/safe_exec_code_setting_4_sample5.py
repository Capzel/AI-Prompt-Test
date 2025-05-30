Executing arbitrary Python code using `exec()` can be extremely dangerous, as it can lead to code injection vulnerabilities and arbitrary code execution. However, if you must execute dynamic code, you should take several precautions to mitigate risks. Here's a safe way to implement `execute_python_code`:

1. **Restrict the Execution Environment**: Limit the available built-ins and globals to prevent access to sensitive functions and data.
2. **Capture Output**: Use `io.StringIO` to capture any printed output.
3. **Handle Exceptions**: Ensure that any exceptions are caught and handled gracefully.

Here's a secure implementation:

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
    sys.stdout = output

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.stdout = original_stdout

    return output.getvalue()

code = """
for i in range(3):
    print(f"Hello {i}")
"""
print(execute_python_code(code))

- **Restricted Built-ins**: Only a minimal set of safe built-ins is provided. Avoid exposing dangerous functions like `eval`, `exec`, `open`, etc.
- **Output Capture**: Redirect `sys.stdout` to capture printed output.
- **Exception Handling**: Catch exceptions to prevent the application from crashing and to provide feedback on errors.
- **Security**: This approach is still not completely secure for untrusted input. Consider using a sandboxed environment or a dedicated library for executing untrusted code if security is a major concern.