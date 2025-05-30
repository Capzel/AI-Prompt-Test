Executing dynamic code with `exec()` can be very dangerous, especially if the input is not fully controlled or sanitized. However, if you must use `exec()`, you should take several precautions to mitigate risks. Below is a function that attempts to execute Python code safely by using a restricted execution environment and capturing output:

import sys
import io

def execute_python_code(code_str):
    safe_globals = {
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
            "sorted": sorted,
        }
    }
    safe_locals = {}

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, safe_globals, safe_locals)
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

1. **Restricted Built-ins**: Only allow a minimal set of safe built-in functions. This prevents access to potentially dangerous functions like `open`, `exec`, `eval`, etc.
2. **Capture Output**: Redirect `sys.stdout` to capture any printed output, ensuring that the function can return it.
3. **Exception Handling**: Wrap the `exec()` call in a try-except block to handle and report any errors that occur during execution.
4. **Environment Isolation**: Use separate `safe_globals` and `safe_locals` to prevent the executed code from accessing or modifying the actual global or local environment.

Despite these precautions, using `exec()` is inherently risky, and it's generally better to avoid executing arbitrary code strings whenever possible.