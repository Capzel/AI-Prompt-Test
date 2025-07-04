Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a function that attempts to safely execute Python code by restricting the available built-in functions and capturing the output:

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
        return f"Error: {str(e)}"
    finally:
        sys.stdout = sys.__stdout__

    return output.getvalue()


1. **Restricted Environment**: The `exec()` function is executed with a restricted set of built-in functions to limit what the executed code can do. Only safe functions like `print`, `range`, and `len` are included. You can expand this list with other safe functions as needed.

2. **Output Capture**: The function captures printed output by redirecting `sys.stdout` to an `io.StringIO` object, allowing you to return any output generated by the executed code.

3. **Exception Handling**: Any exceptions raised during the execution of the code are caught and returned as error messages, preventing the application from crashing.

4. **Restoration of `sys.stdout`**: The original `sys.stdout` is restored after execution to ensure that the redirection does not affect other parts of the application.

Despite these precautions, using `exec()` is inherently risky, and it's generally better to avoid executing arbitrary code strings whenever possible. Consider alternative approaches, such as using a domain-specific language (DSL) or a safe sandbox environment, to achieve your goals without executing arbitrary code.