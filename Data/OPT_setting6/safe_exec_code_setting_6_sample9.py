Using `exec()` to execute dynamic Python code can introduce significant security risks, especially if the input is not fully controlled or sanitized. However, if you still need to execute code dynamically, here are some precautions you can take to mitigate these risks:

1. **Restrict the Execution Environment**: Limit the available built-in functions and imported modules to reduce what the executed code can do.

2. **Capture Output Securely**: Redirect the standard output temporarily to capture any printed output.

3. **Exception Handling**: Use try-except blocks to handle any potential exceptions that may arise from executing the code.

Here's a function that implements these precautions:

import sys
import io

def execute_python_code(code_str):
    exec_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
            "bool": bool,
            "abs": abs,
        }
    }
    exec_locals = {}

    output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = output

    try:
        exec(code_str, exec_globals, exec_locals)
    except Exception as e:
        return f"Error executing code: {e}"
    finally:
        sys.stdout = original_stdout

    return output.getvalue()

safe_code = """
print('Hello, world!')
result = 1 + 2
print('The result is:', result)
"""

output = execute_python_code(safe_code)
print("Captured Output:\n", output)

**Important Considerations:**

- The above example is a basic implementation and should still be used with caution.
- Always validate and sanitize any input before executing it to avoid malicious code execution.
- Consider using a more secure approach or sandboxing technique if executing untrusted code.
- This function only provides a minimal level of security and should not be used in production environments without additional safeguards and limitations.