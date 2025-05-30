Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to code injection vulnerabilities. However, if you absolutely must use it, you should take extreme precautions. Below is an example of how you might do this with some safety measures, but remember that no solution can make `exec()` completely safe against malicious input.

import sys
import io
import traceback

def execute_python_code(code_str):
    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    try:
        restricted_globals = {
            '__builtins__': {
                'print': print,
                'range': range,
                'len': len,
                'int': int,
                'float': float,
                'str': str,
                'bool': bool,
                'list': list,
                'dict': dict,
                'set': set,
                'tuple': tuple,
                'enumerate': enumerate,
                'zip': zip,
                'min': min,
                'max': max,
                'sum': sum,
                'abs': abs,
                'all': all,
                'any': any,
            }
        }
        restricted_locals = {}

        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        traceback.print_exc()
    finally:
        sys.stdout = old_stdout

    return redirected_output.getvalue()

code = """
print("Hello, World!")
for i in range(3):
    print(i)
"""
output = execute_python_code(code)
print("Captured Output:\n", output)

1. **Restricted Environment**: We define a restricted set of built-in functions to limit what the executed code can do. This is not foolproof but can help mitigate some risks.
2. **Output Capture**: We redirect `sys.stdout` to capture any printed output from the executed code.
3. **Exception Handling**: We use a try-except block to capture and print any exceptions that occur during execution, which can help with debugging.
4. **No External Imports**: We don't allow importing of external modules, which limits the potential for harmful operations.

Remember, using `exec()` is inherently risky, and it's best to avoid it if possible. Consider alternative approaches, such as defining a safe subset of operations or using a domain-specific language (DSL) tailored to your needs.