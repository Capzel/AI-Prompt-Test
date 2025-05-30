Executing dynamic code with `exec()` can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a secure implementation that captures printed output and restricts the execution environment:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "str": str,
            "int": int,
            "float": float,
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
    restricted_locals = {}

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, restricted_globals, restricted_locals)
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

1. **Restricted Built-ins**: Only a limited set of safe built-in functions are exposed to the executed code. This prevents access to potentially dangerous functions like `open`, `eval`, `exec`, etc.
2. **Output Capture**: Redirects `stdout` to capture any printed output, allowing you to return it as a string.
3. **Exception Handling**: Catches and returns any exceptions that occur during execution, preventing the application from crashing.

This approach minimizes risk but does not eliminate it entirely. Always consider whether executing dynamic code is necessary and explore safer alternatives if possible.