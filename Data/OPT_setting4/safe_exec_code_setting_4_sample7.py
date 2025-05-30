Executing arbitrary Python code using `exec()` can be extremely dangerous, as it can lead to code injection vulnerabilities and potentially allow an attacker to execute malicious code. However, if you must use `exec()` for a specific use case, you should take several precautions to mitigate risks. Below is a function that attempts to safely execute Python code with some basic precautions:

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

1. **Restricted Built-ins**: Only allow a limited set of safe built-in functions to be used within the executed code. This prevents access to potentially dangerous functions like `open`, `exec`, `eval`, etc.

2. **Output Redirection**: Redirect `stdout` to capture any output from `print` statements within the executed code.

3. **Exception Handling**: Wrap the execution in a try-except block to handle and report any errors that occur during execution.

4. **Namespace Isolation**: Execute the code in a restricted namespace to prevent access to the broader environment.

Despite these precautions, using `exec()` is inherently risky, and it's generally advisable to avoid executing arbitrary code strings whenever possible. If you have control over the code being executed, consider safer alternatives or limit the functionality to specific, well-defined operations.