Executing dynamic code with `exec()` can be very dangerous, especially if the input is not trusted, as it can lead to arbitrary code execution vulnerabilities. However, if you must use `exec()`, you should take several precautions to mitigate risks. Here's a safe approach to implementing `execute_python_code`:

import sys
import io
import traceback

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
            "bool": bool,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
            "enumerate": enumerate,
            "zip": zip,
            "map": map,
            "filter": filter,
            "sum": sum,
            "min": min,
            "max": max,
            "abs": abs,
            "all": all,
            "any": any,
        }
    }
    restricted_locals = {}

    output = io.StringIO()
    sys_stdout = sys.stdout
    sys.stderr = sys.stderr

    try:
        sys.stdout = output
        sys.stderr = output
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        traceback.print_exc(file=output)
    finally:
        sys.stdout = sys_stdout
        sys.stderr = sys.stderr

    return output.getvalue()

code = """
print("Hello, World!")
for i in range(3):
    print(i)
"""
result = execute_python_code(code)
print("Captured Output:\n", result)

1. **Restricted Environment**: Limit the available built-in functions to a safe subset by overriding `__builtins__`. This prevents access to potentially dangerous functions and modules.
2. **Output Capture**: Redirect `sys.stdout` and `sys.stderr` to capture any output or errors produced by the executed code.
3. **Exception Handling**: Use a try-except block to catch and log any exceptions, ensuring that errors do not crash the application and are safely reported.
4. **No External Access**: Avoid providing access to file operations, network operations, or any other potentially harmful operations.

This approach minimizes risk but does not eliminate it entirely. Always be cautious when executing dynamic code, especially if the source is untrusted.