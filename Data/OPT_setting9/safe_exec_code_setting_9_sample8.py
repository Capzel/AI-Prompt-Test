Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it poses significant security risks. It can execute arbitrary code, potentially leading to code injection vulnerabilities, data corruption, or unauthorized access to system resources. Therefore, it's crucial to avoid using `exec()` with untrusted input.

However, if you must execute dynamic code and are aware of the risks, you can take some precautions to mitigate potential harm. Here's a minimal implementation that captures printed output while attempting to restrict the execution environment:

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
    sys_stdout = sys.stdout
    sys.stdout = output

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {e}"
    finally:
        sys.stdout = sys_stdout

    return output.getvalue()

code = """
for i in range(3):
    print(f"Hello {i}")
"""
print(execute_python_code(code))

- **Restricted Environment**: We define a limited set of built-in functions available to the executed code. This helps prevent the execution of potentially harmful functions.
- **Output Capture**: We redirect `sys.stdout` to capture printed output.
- **Error Handling**: We catch exceptions to prevent the application from crashing and return error messages safely.
- **Security Warning**: This approach is still not completely secure. Avoid using `exec()` with untrusted input in production environments. Consider safer alternatives like sandboxing or using a dedicated execution environment.