Executing arbitrary Python code using `exec()` can be extremely dangerous due to the potential for code injection and other security vulnerabilities. However, if you absolutely must execute dynamic code, you should take precautions to mitigate risks. Here's a safe way to handle this:

1. **Limit the execution environment**: Restrict the built-in functions and modules available to the executed code.
2. **Capture output**: Redirect standard output to capture any printed output from the executed code.
3. **Error handling**: Use try-except blocks to handle exceptions gracefully.

Here's an example implementation:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
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
    print(f"Hello {i}")
"""
print(execute_python_code(code))

- **Restricted Environment**: The `restricted_globals` dictionary limits the available built-ins to only those explicitly allowed. This helps prevent access to dangerous functions.
- **Output Capture**: `io.StringIO()` is used to capture the output of the executed code.
- **Error Handling**: The `try-except` block ensures that any exceptions are caught and reported without crashing the program.

Remember, even with these precautions, executing dynamic code should be avoided if possible. Consider safer alternatives, such as pre-defined scripts or a domain-specific language, if applicable.