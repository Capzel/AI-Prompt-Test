Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Here's a basic implementation that captures printed output and includes some safety measures:

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

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, restricted_globals, restricted_locals)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {str(e)}"
    finally:
        sys.stdout = old_stdout

    return output

code = """
print("Hello, World!")
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: Limit the available built-in functions to only those that are safe and necessary.
2. **Separate Scopes**: Use separate dictionaries for global and local scopes to control the execution environment.
3. **Output Capture**: Redirect `sys.stdout` to capture printed output safely.
4. **Exception Handling**: Catch exceptions to prevent the application from crashing and to provide meaningful error messages.

Despite these precautions, using `exec()` is inherently risky, and it's generally recommended to avoid executing arbitrary code strings whenever possible. Consider safer alternatives, such as using a domain-specific language (DSL) or a sandboxed execution environment.