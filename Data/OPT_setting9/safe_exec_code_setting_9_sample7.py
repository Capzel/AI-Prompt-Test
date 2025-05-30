Executing dynamic code with `exec()` can be very dangerous, especially if the input is not fully trusted, as it can lead to arbitrary code execution vulnerabilities. However, if you must use `exec()`, you should take extreme precautions to mitigate risks. Here's a basic implementation that captures printed output and attempts to sandbox the execution environment:

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
print("Hello, World!")
x = 5
print(x * 2)
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: We define a limited set of safe built-in functions to prevent the execution of potentially dangerous operations.
2. **Output Capture**: We redirect `sys.stdout` to capture any output from `print` statements within the executed code.
3. **Error Handling**: We catch exceptions to prevent the application from crashing and to provide feedback on errors.
4. **No External Imports**: The code execution environment does not allow importing external modules, which limits the potential for abuse.

Despite these precautions, using `exec()` is inherently risky. If possible, consider alternative approaches that do not require executing arbitrary code strings.