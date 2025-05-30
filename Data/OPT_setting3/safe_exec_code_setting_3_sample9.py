Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a secure implementation that uses `exec()` with some safety measures:

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

1. **Restricted Built-ins**: Only a limited set of safe built-in functions are exposed to the executed code. This prevents access to potentially dangerous functions like `open`, `exec`, `eval`, etc.

2. **Output Redirection**: `sys.stdout` is redirected to capture any output from `print` statements within the executed code.

3. **Exception Handling**: Any exceptions raised during execution are caught and returned as part of the output, preventing the application from crashing.

4. **No Access to Globals**: The global environment is restricted to only the safe built-ins, preventing access to sensitive data or functions.

Despite these precautions, using `exec()` is inherently risky, and it's generally recommended to avoid executing arbitrary code strings whenever possible. Consider alternative approaches, such as using a domain-specific language (DSL) or a sandboxed environment, for executing user-provided logic.