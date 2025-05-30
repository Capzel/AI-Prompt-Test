Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Here's a secure approach to implementing such a function:

import sys
import io

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
            "abs": abs,
            "sum": sum,
            "min": min,
            "max": max,
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


1. **Restricted Built-ins**: Limit the available built-in functions to a safe subset. This prevents the execution of potentially dangerous functions.
2. **Namespace Isolation**: Use separate dictionaries for global and local namespaces to control what the executed code can access.
3. **Output Capture**: Redirect `sys.stdout` to capture any printed output, ensuring that the function can return it.
4. **Exception Handling**: Catch exceptions to prevent the application from crashing and to provide feedback on errors.

This approach significantly reduces the risk but does not eliminate it entirely. Always consider whether executing arbitrary code is truly necessary and explore safer alternatives if possible.