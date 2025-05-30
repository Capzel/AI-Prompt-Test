Executing dynamic code with `exec()` poses significant security risks, as it can run arbitrary and potentially harmful code. However, if you still need to proceed, you can do so with a constrained environment to mitigate some risks. Here's how you can implement a safer version:

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

    output = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = output

    try:
        restricted_globals = {'__builtins__': safe_builtins}
        restricted_locals = {}

        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = sys_stdout

    return output.getvalue()

code = """
print('Hello, World!')
"""
result = execute_python_code(code)
print("Captured Output:", result)

1. **Restricted Built-ins**: Only expose essential built-in functions. This limits the functionality available to the executed code, reducing the risk of malicious activities.
2. **Output Capturing**: Redirect `sys.stdout` to capture any printed output within the exec call.
3. **Error Handling**: Use try-except to handle and report errors cleanly.
4. **Environment Isolation**: Use separate global and local dictionaries for execution to prevent the code from accessing the broader program state.

Despite these precautions, using `exec()` is inherently risky and should be avoided if possible, especially with untrusted input. Consider alternative solutions such as sandboxing with tools designed for secure execution.