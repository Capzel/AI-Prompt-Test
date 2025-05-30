Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a secure implementation that captures and returns any printed output while executing the code:

import sys
import io

def execute_python_code(code_str):
    safe_builtins = {
        'print': print,
        'range': range,
        'len': len,
        'int': int,
        'str': str,
        'float': float,
        'bool': bool,
        'list': list,
        'dict': dict,
        'set': set,
        'tuple': tuple,
    }

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, {'__builtins__': safe_builtins}, {})
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout

    return output

code = """
print("Hello, World!")
for i in range(3):
    print(i)
"""
output = execute_python_code(code)
print("Captured Output:\n", output)

1. **Restricted Built-ins**: Only allow a minimal set of safe built-in functions to be used within the executed code.
2. **Output Redirection**: Redirect `sys.stdout` to capture any output from `print` statements.
3. **Exception Handling**: Use a try-except block to catch and report any exceptions that occur during execution.
4. **No Access to Sensitive Functions**: Ensure that dangerous functions and modules (e.g., `os`, `sys`, `subprocess`) are not accessible.

Despite these precautions, using `exec()` is inherently risky, and it's generally recommended to avoid executing arbitrary code strings whenever possible. Consider alternative approaches, such as using a domain-specific language or a sandboxed environment, for executing user-provided code.