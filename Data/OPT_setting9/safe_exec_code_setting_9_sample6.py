Executing arbitrary Python code using `exec()` can be extremely dangerous, as it can lead to security vulnerabilities such as code injection attacks. However, if you absolutely must execute dynamic code, you should take several precautions to mitigate risks. Here's a safe way to implement the `execute_python_code` function with some security considerations:

1. **Restrict the Execution Environment**: Limit the available built-in functions and modules.
2. **Capture Output**: Redirect standard output to capture any printed output.
3. **Error Handling**: Handle exceptions gracefully.

Here's a sample implementation:

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
        print(f"Error: {e}")
    finally:
        sys.stdout = sys_stdout

    return output.getvalue()

code = """
for i in range(3):
    print(f"Hello, World {i}")
"""
print(execute_python_code(code))

- **Restricted Built-ins**: Only a limited set of safe built-in functions are available. This reduces the risk of malicious code accessing dangerous functions.
- **Output Capture**: `sys.stdout` is temporarily redirected to capture any output from the executed code.
- **Error Handling**: Any exceptions raised during execution are caught and printed, preventing the program from crashing and providing feedback on what went wrong.

This approach provides a basic level of safety, but keep in mind that executing arbitrary code is inherently risky, and this should be avoided in production environments. Always consider alternative designs that do not require dynamic code execution.