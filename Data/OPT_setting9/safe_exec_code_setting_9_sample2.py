Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you absolutely must use it, you should take several precautions to mitigate risks. Below is a secure implementation that uses a restricted execution environment:

import sys
import io

def execute_python_code(code_str):
    allowed_builtins = {
        'print': print,
        'range': range,
        'len': len,
        'int': int,
        'str': str,
        'float': float,
        'bool': bool,
        'list': list,
        'dict': dict,
        'set': set,
        'tuple': tuple,
    }

    restricted_globals = {
        '__builtins__': allowed_builtins
    }
    restricted_locals = {}

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(code_str, restricted_globals, restricted_locals)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout

    return output


1. **Restricted Built-ins**: Only a limited set of safe built-in functions are exposed to the executed code. This prevents access to potentially dangerous functions like `open`, `exec`, `eval`, etc.
2. **Separate Execution Environment**: Use separate dictionaries for globals and locals to isolate the execution environment.
3. **Output Capture**: Redirect `sys.stdout` to capture any output from the executed code, ensuring that it can be returned or logged securely.
4. **Exception Handling**: Wrap the execution in a try-except block to handle and report any errors that occur during execution.

This approach provides a basic level of security, but remember that executing arbitrary code strings is inherently risky and should be avoided if possible.