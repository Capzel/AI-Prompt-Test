Executing dynamic code with `exec()` can be very dangerous, especially if the input is not fully controlled or sanitized. However, if you must use it, here is a way to do it with some precautions:

1. **Restrict the Execution Environment**: Limit the available built-in functions and variables.
2. **Capture Output**: Redirect standard output to capture any printed output.
3. **Exception Handling**: Ensure that any exceptions are caught and handled appropriately.

Here's a basic implementation:

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
    print(f"Number: {i}")
"""
print(execute_python_code(code))

- **Restricted Environment**: The `__builtins__` dictionary is limited to only a few safe functions. This reduces the risk of executing harmful code.
- **Output Capture**: The `io.StringIO` object is used to capture any output that would normally be printed to the console.
- **Exception Handling**: Any exceptions raised during execution are caught and printed, preventing the program from crashing.

**Note**: This approach is still not completely secure against all possible attacks, especially if the input is from an untrusted source. Consider using a more secure method or sandboxing techniques if possible.