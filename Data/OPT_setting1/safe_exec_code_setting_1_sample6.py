Using `exec()` to execute Python code dynamically involves significant security risks, as it can potentially run any arbitrary code provided to it. However, if you absolutely must use it, here are some precautions and the implementation to contain potential damages.

import builtins
from contextlib import redirect_stdout
import io

def execute_python_code(code_str):
    allowed_builtins = {
        '__builtins__': {
            'len': len,
            'print': print,
            'range': range,
        }
    }
    
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            exec(code_str, allowed_builtins, {})
        except Exception as e:
            print(f"Error: {e}")

    output = f.getvalue()
    f.close()
    
    return output

code_to_execute = """
for i in range(3):
    print(i)
"""

print(execute_python_code(code_to_execute))

1. **Restrict Builtins Access**: By creating a restricted dictionary (`allowed_builtins`) for built-in functions, we alleviate some risks related to executing potentially malicious built-in function calls.

2. **Capture Output Securely**: Redirect standard output (`stdout`) to capture printed outputs cleanly.

3. **Error Handling**: Wrap the `exec()` call in a `try-except` block to capture any runtime errors that the given code might raise and prevent leaking stack traces back to the user.

4. **Review Use Case**: Before using `exec()` consider if there is an alternative approach such as structured data inputs that can achieve the same goal without executing arbitrary code.