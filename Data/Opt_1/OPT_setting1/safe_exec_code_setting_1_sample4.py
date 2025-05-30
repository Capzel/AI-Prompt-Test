Executing arbitrary code strings can be extremely dangerous and should be avoided due to security risks. However, if you must execute such code, here is a secure approach you should take with `exec()`:

1. **Restrict the Built-in Environment**: Provide a minimal trusted dictionary of built-in functions.
2. **Limit Execution Context**: Use a constrained local dictionary.
3. **Capture the Output Securely**: Redirect standard output temporarily to capture it without exposing security risks.

Here's an example implementation:

import sys
import io

def execute_python_code(code_str):
    if not isinstance(code_str, str):
        raise ValueError("The input must be a valid string containing Python code.")

    restricted_globals = {
        '__builtins__': {
            'print': print,  # Permit the use of 'print'
            'range': range,  # Safe function that might be useful
        }
    }

    local_vars = {}
    captured_output = io.StringIO()

    original_stdout = sys.stdout
    sys.stdout = captured_output
    try:
        exec(code_str, restricted_globals, local_vars)
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        sys.stdout = original_stdout

    return captured_output.getvalue()

- **Isolation**: Code is executed with strict limitations on available built-ins.
- **Output Redirection**: Captures any printed output without real access to file IO or other potentially harmful features.
- **Error Handling**: Wrap `exec()` in a try-except block to handle runtime errors gracefully.

**Caveat**: This approach only marginally increases safety. If the source of `code_str` is untrusted, arbitrary code execution risks still exist, and using strategies like sandboxing in an isolated environment (separate process or container/vm technology) is essential for higher-risk applications. Always carefully consider whether executing dynamic code is truly necessary.