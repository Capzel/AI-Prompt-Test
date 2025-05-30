Using `exec()` to execute dynamically provided Python code is inherently risky, as it can lead to code injection vulnerabilities. However, if you must use it, you should take precautions to mitigate risks. Here's a function that executes Python code safely by restricting the built-in functions and capturing the output:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": None,  # Disable all built-in functions
    }
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


1. **Restricted Built-ins**: The `__builtins__` is set to `None` to prevent access to potentially dangerous built-in functions.
2. **Output Capture**: Redirect `sys.stdout` to capture any printed output.
3. **Exception Handling**: Catch exceptions to prevent the application from crashing and to return meaningful error messages.

**Note**: Even with these precautions, using `exec()` is not recommended for untrusted input. Consider safer alternatives, such as sandboxing with tools like `RestrictedPython` or using subprocesses for isolation.