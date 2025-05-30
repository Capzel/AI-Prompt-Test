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


1. **Restricted Environment**: The `restricted_globals` dictionary limits the available built-in functions to a safe subset, preventing access to potentially dangerous functions like `open`, `exec`, `eval`, etc.
2. **Output Capture**: Redirects `sys.stdout` to capture any printed output from the executed code.
3. **Error Handling**: Catches exceptions and returns them as part of the output, preventing the application from crashing.
4. **Security Caveats**: Despite these precautions, using `exec()` is inherently risky. Consider alternative approaches, such as using a sandboxed environment or a dedicated library for executing untrusted code.