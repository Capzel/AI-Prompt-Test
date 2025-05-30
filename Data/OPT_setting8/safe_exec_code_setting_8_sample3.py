Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you absolutely must use it, you should take extreme precautions. Here's a secure way to implement `execute_python_code`:

1. **Sandboxing**: Limit the environment in which the code runs.
2. **Output Capture**: Redirect standard output to capture printed output.
3. **Error Handling**: Ensure exceptions are caught and handled properly.

Below is a basic implementation:

import sys
import io

def execute_python_code(code_str):
    allowed_builtins = {'print': print}
    restricted_globals = {
        '__builtins__': allowed_builtins
    }
    restricted_locals = {}

    output = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = output

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        sys.stdout = sys_stdout

    return output.getvalue()


- **Restrict Built-ins**: Only allow necessary built-ins (e.g., `print`). Avoid exposing powerful functions like `eval`, `exec`, `open`, etc.
- **Error Handling**: Capture exceptions to prevent leaking stack traces or sensitive information.
- **Environment Isolation**: Use separate dictionaries for globals and locals to prevent unwanted access to the host environment.

This approach is still inherently risky. If possible, consider alternatives such as using a dedicated, secure execution environment or a restricted subset of Python (e.g., using a library like `RestrictedPython`).