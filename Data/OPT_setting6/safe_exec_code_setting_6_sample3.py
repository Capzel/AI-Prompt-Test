Executing arbitrary Python code dynamically, especially using `exec()`, poses significant security risks and is generally discouraged in production environments. However, if you absolutely must execute code dynamically, you should employ strict precautions. Here's an example of how you might attempt this safely:

import sys
import io

def execute_python_code(code_str):
    if not isinstance(code_str, str):
        raise ValueError("Code must be a string.")

    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        restricted_globals = {
            "__builtins__": {
                "print": print,
                "range": range,
            }
        }
        restricted_locals = {}

        exec(code_str, restricted_globals, restricted_locals)

        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {str(e)}"
    finally:
        sys.stdout = original_stdout

    return output


**Key Points:**
- **Security Concerns**: This function assumes the input code is from a trusted source. Untrusted code can lead to security vulnerabilities, including arbitrary code execution.
- **Restricted Environment**: We define a minimal set of built-ins in `restricted_globals` to limit what the executed code can access.
- **Output Capture**: We use `io.StringIO` to capture any printed output during the execution.
- **Error Handling**: Exceptions are caught and returned as part of the output, which helps in diagnosing issues without crashing.
- **Code Validation**: In a real-world scenario, consider implementing more robust code validation or sandboxing mechanisms.

**Caution**: This approach is inherently risky, and you should avoid executing untrusted code whenever possible. Consider safer alternatives such as using a scripting language with better sandboxing features or running code in a dedicated, isolated environment.