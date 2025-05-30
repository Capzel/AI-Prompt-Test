Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take significant precautions to mitigate the risks. Below is a secure implementation that captures and returns any printed output while executing the code:

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

1. **Restricted Built-ins**: We provide a limited set of safe built-in functions to the execution environment to prevent access to dangerous functions like `open`, `exec`, `eval`, etc.
2. **Output Redirection**: We redirect `sys.stdout` to capture any printed output from the executed code.
3. **Exception Handling**: We wrap the execution in a try-except block to catch and report any errors that occur during execution.
4. **Minimal Built-in Access**: We ensure that the code execution environment has no access to sensitive built-ins or the broader environment.

Despite these precautions, executing arbitrary code remains inherently risky. Always consider safer alternatives, such as using a dedicated sandbox environment or a restricted execution framework.