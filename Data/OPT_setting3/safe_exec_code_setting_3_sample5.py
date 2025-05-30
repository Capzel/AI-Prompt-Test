Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a function that attempts to execute Python code safely by using a restricted execution environment and capturing output:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "str": str,
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


1. **Restricted Built-ins**: Only a limited set of safe built-in functions are exposed to the executed code. This helps prevent the code from performing dangerous operations.
2. **Output Capture**: The function captures printed output using `io.StringIO()` to redirect `sys.stdout`.
3. **Exception Handling**: Any exceptions during execution are caught and returned as part of the output, preventing the application from crashing.

Despite these precautions, using `exec()` is inherently risky, and it's generally better to avoid executing arbitrary code strings whenever possible. Consider alternative approaches, such as using a domain-specific language (DSL) or a sandboxed environment, for executing user-provided logic.