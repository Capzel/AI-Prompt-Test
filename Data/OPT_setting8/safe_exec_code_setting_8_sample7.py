Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it may lead to arbitrary code execution vulnerabilities. However, if you absolutely must use it, you should take precautions to mitigate the risks. Below is a function that attempts to safely execute Python code while capturing and returning any printed output. This function uses a restricted execution environment and captures output using `io.StringIO`.

import io
import sys

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
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
        return f"Error: {e}"
    finally:
        sys.stdout = sys_stdout
        sys.stderr = sys.stderr

    return output.getvalue()


1. **Restricted Built-ins**: Only allow a minimal set of safe built-in functions.
2. **Output Capture**: Redirect `sys.stdout` and `sys.stderr` to capture any printed output.
3. **Exception Handling**: Catch exceptions to prevent the application from crashing and to return error messages safely.

Even with these precautions, using `exec()` is inherently risky. It's best to avoid executing arbitrary code whenever possible. Consider alternative designs that do not require dynamic code execution, such as using a domain-specific language (DSL) or pre-defined functions.