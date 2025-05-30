Executing arbitrary Python code using `exec()` can introduce significant security risks, such as code injection and unauthorized access to system resources. Therefore, it's important to carefully sandbox the execution environment and limit the capabilities of the executed code.

Here's a safe approach to implementing such a function:

import sys
import io
import traceback

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
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
        output.write(traceback.format_exc())
    finally:
        sys.stdout = sys_stdout
        sys.stderr = sys.stderr

    return output.getvalue()


1. **Restricted Environment:** Limit the available built-in functions to only those that are safe and necessary. Avoid exposing dangerous functions like `open`, `eval`, or `exec`.
2. **Capture Outputs:** Redirect `stdout` and `stderr` to capture what the executed code prints or any errors it raises.
3. **Exception Handling:** Catch exceptions and capture their tracebacks to prevent the program from crashing and provide useful error messages.
4. **Review Input:** Always ensure that the input to this function is from a trusted source, as even with precautions, executing arbitrary code can be inherently risky.

This implementation is a basic approach and may not be fully secure for all use cases. For untrusted code execution, consider using more robust solutions like containerization or dedicated sandbox environments.