Executing dynamic code using `exec()` can be highly dangerous, especially if the input is not fully trusted. However, if you must use `exec()`, you should take several precautions to mitigate risks. Below is a secure implementation that uses a restricted execution environment and captures printed output:

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


1. **Restricted Built-ins**: Only a limited set of safe built-in functions are exposed to the executed code. This prevents access to potentially dangerous functions like `open`, `exec`, `eval`, etc.
2. **Isolated Environment**: The code is executed with separate `safe_globals` and `safe_locals` to prevent it from accessing or modifying the main program's environment.
3. **Output Capture**: Redirects `stdout` to capture any printed output, ensuring that the function can return it.

This approach minimizes risk but does not eliminate it entirely. Always validate and sanitize input, and consider alternative designs that do not require dynamic code execution.