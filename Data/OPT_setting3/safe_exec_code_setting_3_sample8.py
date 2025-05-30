Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a function that attempts to execute Python code safely by using a restricted execution environment and capturing output:

import sys
import io

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
    sys.stdout = output

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = sys.__stdout__

    return output.getvalue()


1. **Restricted Environment**: The `exec()` function is executed with a restricted set of built-in functions to limit what the executed code can do. Only safe functions like `print`, `range`, and `len` are included. You can expand this list with other safe functions as needed.

2. **Output Capture**: The function captures any output printed by the executed code using `io.StringIO()` and temporarily redirects `sys.stdout`.

3. **Error Handling**: Any exceptions raised during execution are caught and returned as error messages.

4. **Security Warning**: Despite these precautions, using `exec()` is inherently risky. Avoid using it with untrusted input. Consider alternative approaches, such as using a domain-specific language (DSL) or a sandboxed execution environment, for executing dynamic code safely.