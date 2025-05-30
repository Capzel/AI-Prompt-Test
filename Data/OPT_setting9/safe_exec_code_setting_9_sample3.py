Executing arbitrary Python code using `exec()` can be extremely dangerous due to the potential for code injection and other security vulnerabilities. However, if you absolutely must execute dynamic code, you should take several precautions to mitigate risks. Here's a safe approach to implementing such a function:

import sys
import io
import traceback

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
        'abs': abs,
        'sum': sum,
        'min': min,
        'max': max,
        'all': all,
        'any': any,
    }

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, {'__builtins__': safe_builtins}, {})
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {traceback.format_exc()}"
    finally:
        sys.stdout = old_stdout

    return output


1. **Restricted Built-ins**: Limit the available built-in functions to a safe subset to prevent access to potentially dangerous functions.
2. **Output Redirection**: Redirect `stdout` to capture and return any printed output.
3. **Exception Handling**: Use a try-except block to handle and report any exceptions that occur during execution.
4. **No Access to Sensitive Functions**: Ensure that sensitive functions and modules (e.g., `os`, `sys`, `subprocess`) are not accessible.

This approach significantly reduces the risk but does not eliminate it entirely. Always carefully consider the security implications before executing dynamic code.