Executing dynamic code using `exec()` can be extremely dangerous, especially if the input is not fully trusted, as it can lead to arbitrary code execution vulnerabilities. However, if you must use `exec()`, you should take several precautions to mitigate risks. Below is a secure implementation that captures and returns any printed output while minimizing potential security risks:

import sys
import io

def execute_python_code(code_str):
    safe_builtins = {
        'print': print,
        'range': range,
        'len': len,
        'int': int,
        'float': float,
        'str': str,
        'bool': bool,
        'list': list,
        'dict': dict,
        'set': set,
        'tuple': tuple,
        'enumerate': enumerate,
        'zip': zip,
        'abs': abs,
        'min': min,
        'max': max,
        'sum': sum,
        'all': all,
        'any': any,
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
for i in range(3):
    print(i)
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: We define a limited set of safe built-in functions to prevent access to potentially dangerous functions and modules.
2. **Output Capture**: We redirect `sys.stdout` to capture any output from `print` statements within the executed code.
3. **Error Handling**: We wrap the execution in a try-except block to handle any exceptions gracefully and return an error message.
4. **No Access to Sensitive Functions**: By not including functions like `open`, `exec`, `eval`, or any module imports, we reduce the risk of file system access or further code execution.

Despite these precautions, it's crucial to understand that executing arbitrary code strings is inherently risky. Always validate and sanitize inputs, and avoid using `exec()` whenever possible in production environments.