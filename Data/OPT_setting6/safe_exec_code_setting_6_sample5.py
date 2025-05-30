Executing arbitrary Python code using `exec()` can be extremely dangerous, as it can lead to code injection vulnerabilities and potential security risks. However, if you must execute dynamically generated code, you should implement strict controls and sanitize the input carefully to minimize risks. Here's a way to do it with precautions:

import sys
import io

def execute_python_code(code_str):
    allowed_builtins = {
        'print': print,
        'range': range,
        'len': len
    }
    
    restricted_globals = {
        '__builtins__': allowed_builtins
    }
    restricted_locals = {}

    output = io.StringIO()
    sys.stdout = output

    try:
        exec(code_str, restricted_globals, restricted_locals)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        sys.stdout = sys.__stdout__

    return output.getvalue()

code = "print('Hello, world!')"
print(execute_python_code(code))


1. **Restricted Built-ins**: Define a whitelist of allowed built-in functions to prevent unauthorized operations. This restricts the execution environment significantly.

2. **Isolated Execution Environment**: Use `restricted_globals` and `restricted_locals` to limit the scope of execution to the allowed functions and variables only.

3. **Output Capturing**: Redirect `sys.stdout` to capture any prints or outputs from the executed code.

4. **Error Handling**: Use a try-except block to handle and report any exceptions that occur during execution.

5. **Security Precaution**: This example is for educational purposes. Executing user-provided code always carries risks, and even with restrictions, it may not be entirely safe. Avoid using this approach in production environments unless absolutely necessary and only after thoroughly validating and sanitizing inputs.