Executing dynamic code using `exec()` can be highly dangerous, especially if the input is not fully trusted. However, if you must use it, you should take several precautions to mitigate risks. Below is a secure implementation that uses `exec()` with some safety measures:

import sys
import io

def execute_python_code(code_str):
    allowed_builtins = {'print': print, 'range': range, 'len': len}

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
        print(f"Error: {e}")
    finally:
        sys.stdout = sys_stdout

    return output.getvalue()

code = """
print("Hello, World!")
for i in range(3):
    print(i)
"""
print(execute_python_code(code))

1. **Restricted Built-ins**: Only a minimal set of safe built-in functions are exposed to the executed code. This limits what the code can do.
2. **Restricted Environment**: The `exec()` function is executed with restricted global and local dictionaries to prevent access to the full Python environment.
3. **Output Capture**: The `sys.stdout` is temporarily redirected to capture any printed output, ensuring that the function can return it.
4. **Exception Handling**: Any exceptions raised during execution are caught and printed, preventing the application from crashing and providing feedback on errors.

Despite these precautions, using `exec()` should be avoided if possible, especially with untrusted input. Consider alternative approaches such as using a domain-specific language (DSL) or a sandboxed execution environment for safer code execution.