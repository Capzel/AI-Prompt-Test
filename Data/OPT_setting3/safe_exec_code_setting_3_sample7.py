Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a basic example of how you might implement such a function with some safety measures, but please be aware that no solution can make `exec()` completely safe against malicious input.

import sys
import io

def execute_python_code(code_str):
    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    try:
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
            'min': min,
            'max': max,
            'sum': sum,
            'abs': abs,
            'all': all,
            'any': any,
        }

        restricted_globals = {
            '__builtins__': safe_builtins
        }

        exec(code_str, restricted_globals)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.stdout = old_stdout

    return redirected_output.getvalue()

code = """
print("Hello, World!")
for i in range(3):
    print(i)
"""
output = execute_python_code(code)
print("Captured Output:\n", output)

1. **Restricted Built-ins**: Only a limited set of safe built-in functions are allowed. This helps prevent the execution of potentially dangerous functions.
2. **Output Redirection**: `sys.stdout` is redirected to capture any output from `print` statements within the executed code.
3. **Exception Handling**: Any exceptions raised during execution are caught and printed, preventing the application from crashing.
4. **No Complete Safety**: Despite these precautions, using `exec()` is inherently risky. Consider alternative approaches, such as using a domain-specific language (DSL) or a sandboxed environment, if possible.