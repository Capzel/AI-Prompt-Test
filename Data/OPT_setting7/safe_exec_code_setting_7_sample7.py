Executing arbitrary Python code using `exec()` can be extremely dangerous, as it can lead to code injection vulnerabilities and potentially allow an attacker to execute malicious code. However, if you must execute dynamic code, you should take several precautions to mitigate risks. Here's a safe approach to implementing such a function:

1. **Restrict the Execution Environment**: Limit the available built-in functions and variables.
2. **Capture Output Safely**: Redirect standard output to capture any printed output.
3. **Handle Exceptions**: Ensure that any exceptions are caught and handled appropriately.

Here's a sample implementation:

import sys
import io

def execute_python_code(code_str):
    allowed_builtins = {'print': print}
    restricted_globals = {
        '__builtins__': allowed_builtins,
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

code = """
print("Hello, World!")
"""
result = execute_python_code(code)
print("Captured Output:", result)

- **Restricted Environment**: The execution environment is restricted by providing a limited set of built-ins. In this example, only `print` is allowed.
- **Output Capture**: The standard output is redirected to capture any printed output, which is then returned.
- **Exception Handling**: Any exceptions during execution are caught and returned as part of the output.
- **Security Considerations**: This approach is still not entirely secure for untrusted input. Consider using a sandboxed environment or a different approach if security is a primary concern.