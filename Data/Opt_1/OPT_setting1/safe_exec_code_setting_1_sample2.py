Executing arbitrary Python code using `exec()` can pose significant security risks. Even when done with precautions, this approach should generally be avoided in production environments unless absolutely necessary. The use of such code execution should be restricted to trusted inputs only. Here's a safe way to execute Python code strings with output capture, employing limited safety precautions:

import sys
import io
import traceback

def execute_python_code(code_str, safe_globals=None):
    """Executes a given Python code string and returns any printed output."""
    if safe_globals is None:
        safe_globals = {}
    
    stdout_capture = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = stdout_capture

    try:
        exec(code_str, {"__builtins__": None}, safe_globals)
    except Exception as e:
        traceback.print_exc(file=stdout_capture)
    finally:
        sys.stdout = old_stdout

    return stdout_capture.getvalue()

code_sample = """
print('This is safe execution.')
"""
output = execute_python_code(code_sample)
print('Captured:', output)

- **Restricted Builtins:** A minimal `__builtins__` dictionary is passed as the global namespace to limit exposed built-in functions. This approach disables access to dangerous functions by not providing them.
- **Globals Control:** Only a safe, optional `safe_globals` dictionary is provided for potential external variables.
- **Output Capturing:** Redirects `sys.stdout` to capture print statements. Errors are similarly captured using `traceback`, ensuring feedback is available.
- **Error Handling:** Any exceptions generated during execution are caught and the traceback is captured.

Again, be cautious, and strongly consider alternative architectures when working with user-defined code, such as containerization or using dedicated script execution frameworks.