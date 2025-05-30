Using `exec()` to execute dynamically provided code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must proceed, it's essential to implement strict controls and understand the risks involved. Here's a basic approach that captures output safely and limits the execution environment:

import sys
import io
import builtins

def execute_python_code(code_str):
    output = io.StringIO()
    sys_stdout_original = sys.stdout
    sys.stdout = output

    try:
        restricted_globals = {
            '__builtins__': {
                'print': print,
                'range': range,
            }
        }
        
        exec(code_str, restricted_globals)
        
    finally:
        sys.stdout = sys_stdout_original

    return output.getvalue()

code = "print('Hello, World!')"
print(execute_python_code(code))


1. **Restricted Environment**: We limit the available built-ins to only those functions that are deemed safe. This prevents the execution of dangerous functions like `eval()` or `open()`.

2. **Capture Output**: We redirect `sys.stdout` to capture the output of the executed code, preventing it from being printed directly to the console.

3. **Minimal Built-ins**: Populate `restricted_globals['__builtins__']` with only the necessary built-ins. Avoid exposing powerful functions and modules.

4. **Awareness of Risks**: Even with these precautions, executing arbitrary code poses significant security risks. Avoid using this in a production environment unless absolutely necessary and ensure the input is fully trusted.

This approach minimizes risk but does not eliminate it entirely. For safer alternatives, consider designing the application so that this type of dynamic execution isn't required.