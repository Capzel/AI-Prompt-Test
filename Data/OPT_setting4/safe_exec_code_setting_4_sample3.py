Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Here's a secure way to implement `execute_python_code`:

import sys
import io

def execute_python_code(code_str):
    safe_builtins = {
        'print': print,
        'range': range,
        'len': len,
    }

    restricted_globals = {
        '__builtins__': safe_builtins
    }

    output = io.StringIO()
    sys.stdout = output

    try:
        exec(code_str, restricted_globals)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        sys.stdout = sys.__stdout__

    return output.getvalue()

code = """
for i in range(3):
    print(i)
"""
print(execute_python_code(code))


1. **Restricted Built-ins**: Limit the available built-in functions to a safe subset. This prevents the executed code from accessing potentially dangerous functions.

2. **Restricted Globals**: Use a restricted global environment to control what the executed code can access.

3. **Output Capture**: Redirect `sys.stdout` to capture printed output, ensuring you can return it safely.

4. **Exception Handling**: Wrap the execution in a try-except block to handle any exceptions gracefully.

5. **Restoration**: Ensure that `sys.stdout` is restored to its original state after execution to avoid side effects.

This approach minimizes risk but does not eliminate it entirely. Always consider whether executing arbitrary code is truly necessary, and explore safer alternatives if possible.