Executing arbitrary Python code using `exec()` poses significant security risks, as it can allow execution of malicious code. Nonetheless, if there's a necessity to dynamically execute code, you MUST sandbox the execution environment as much as possible. A relatively safer approach involves the use of a separate namespace, restricting built-in functions, and capturing output through redirection. However, I want to emphasize that there's no foolproof way to execute arbitrary code securely, especially if the code source isn't trusted. Here's a safer approach:

import io
import sys

def execute_python_code(code_str):
    safe_globals = {"__builtins__": None}
    safe_locals = {}

    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, safe_globals, safe_locals)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error during execution: {e}"
    finally:
        sys.stdout = original_stdout
    
    return output


- **Remove Built-ins Access:** `__builtins__` is set to `None` to prevent access to Python’s default built-in functions, reducing the attack surface.
- **Capture stdout:** Redirect standard output before execution and capture printed outputs.
- **Error Handling:** Catch exceptions during execution to gracefully return error messages instead of crashing.
- **Caution:** Despite these precautions, evaluating untrusted code represents a substantial risk. Consider safer alternatives such as Comprehensive AST parsing for specific requirements instead of `exec()`.