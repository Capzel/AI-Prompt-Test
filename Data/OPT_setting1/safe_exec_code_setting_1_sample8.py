While executing code dynamically using `exec()` is inherently risky, here is a way to mitigate some potential security issues by limiting the available built-ins, restricting what can be accessed, and capturing the output:

import sys
import builtins
from io import StringIO

def execute_python_code(code_str):
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    safe_builtins = {
        'print': print,
        'range': range,
        'len': len,
        'int': int,
    }

    restricted_globals = {
        '__builtins__': safe_builtins
    }
    restricted_locals = {}

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        print(f"Error during execution: {e}")

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    return output

code_str = """
for i in range(3):
    print(i)
"""

output = execute_python_code(code_str)
print("Captured Output:\n", output)

1. **Limited Built-ins:** The function only exposes a subset of safe built-in functions. Add more as necessary but always assess the security risks when exposing any new functionalities.
   
2. **Safe Globals and Locals:** The execution context is restricted through `restricted_globals` and `restricted_locals`, preventing access to the execution environment and maintaining strict separation from untrusted code.

3. **Output Redirection:** Uses `StringIO` to safely capture print outputs, as `stdout` is redirected temporarily.

Even with these precautions, using `exec()` is discouraged in production systems where untrusted input is involved as it always carries risk. You should evaluate whether there is a safer alternative to achieve the end goal without executing code dynamically.