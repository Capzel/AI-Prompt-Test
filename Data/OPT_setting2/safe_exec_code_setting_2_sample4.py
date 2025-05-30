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
        }
    }
    
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, restricted_globals)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout

    return output


1. **Restricted Environment**: The `restricted_globals` dictionary limits the available built-in functions to a safe subset, preventing access to potentially dangerous functions like `open`, `exec`, `eval`, etc.

2. **Output Capture**: Redirects `sys.stdout` to capture any printed output, allowing you to return it as a string.

3. **Error Handling**: Catches exceptions to prevent the application from crashing and provides feedback on errors.

Despite these precautions, using `exec()` is inherently risky. Consider alternative approaches, such as using a domain-specific language (DSL) or a sandboxed environment, for executing untrusted code.