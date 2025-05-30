Executing arbitrary Python code using `exec()` can be extremely dangerous due to the potential for code injection and other security vulnerabilities. However, if you absolutely must execute dynamic code, you should take several precautions to mitigate risks. Here's a safe approach to doing this:

1. **Restrict the execution environment**: Limit the available built-in functions and variables.
2. **Capture output safely**: Redirect standard output to capture any printed output.
3. **Use exception handling**: Catch and handle exceptions to prevent the application from crashing.

Below is a Python function that implements these precautions:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {
        '__builtins__': {
            'print': print,
            'range': range,
            'len': len,
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

- **Restricted Environment**: We limit the `__builtins__` to only a few safe functions. This prevents the executed code from accessing potentially dangerous functions.
- **Output Capture**: We redirect `sys.stdout` to capture printed output, which is then returned by the function.
- **Exception Handling**: We catch any exceptions that occur during execution and print an error message.

Remember, even with these precautions, executing dynamic code can still pose risks. Always validate and sanitize any input that could be used to construct the code string, and consider whether executing dynamic code is truly necessary for your application.