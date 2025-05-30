Executing arbitrary code using `exec()` can be highly dangerous, as it allows for potential execution of malicious code. If you must dynamically execute code for educational or controlled environments, you need to take numerous precautions and understand the risks involved.

Here's a minimal implementation that demonstrates a safer way to execute Python code, with some essential precautions:

import traceback

def execute_python_code(code_str):
    safe_locals = {}
    
    import io
    import contextlib

    output_buffer = io.StringIO()
    
    try:
        with contextlib.redirect_stdout(output_buffer):
            exec(code_str, {"__builtins__": {}}, safe_locals)
    except Exception:
        error_msg = f"Error executing code:\n {traceback.format_exc()}"
        return error_msg
    
    return output_buffer.getvalue()

output = execute_python_code(
    """
for i in range(3):
    print(f"Hello {i}")
""")
print(output)


- **Restricted `__builtins__`:** We passed an empty dictionary assigned to `__builtins__` to prevent access to Python's standard libraries, which restricts the capabilities of the executed code to access potentially dangerous functions and modules.
  
- **Exception Handling:** Using `try-except` to catch and handle any exceptions arising during code execution, preventing unexpected crashes.

- **Output Redirection:** Captured the output of print statements using `io.StringIO()` within a context manager `contextlib.redirect_stdout()`.


Even with these precautions, code execution through `exec` still exposes significant risks:

- It could unintentionally consume resources in denial-of-service fashion.
- Still possible to implement somewhat harmful code in creative ways.

It's crucial to use such a function only in severely restricted or trusted environments. If possible, consider utilizing a different approach for executing dynamic code that isolates risk better, such as using containers or a sandboxed environment specifically designed to handle untrusted code execution.