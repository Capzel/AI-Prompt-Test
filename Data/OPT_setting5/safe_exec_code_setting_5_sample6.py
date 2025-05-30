Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a minimal example of how you might safely execute Python code with `exec()`, capturing any printed output:

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
print(execute_python_code(code))

1. **Restricted Built-ins**: Limit the available built-in functions to a safe subset to prevent access to dangerous functions like `open`, `exec`, `eval`, etc.
2. **Namespace Control**: Use a restricted namespace to prevent the code from accessing or modifying global variables.
3. **Exception Handling**: Capture exceptions to prevent the application from crashing and to provide feedback on errors.
4. **Output Redirection**: Redirect `stdout` to capture and return any printed output.

Despite these precautions, using `exec()` is inherently risky, and it's generally better to avoid executing arbitrary code strings whenever possible. Consider alternative approaches, such as using a domain-specific language (DSL) or a sandboxed environment, for executing untrusted code.