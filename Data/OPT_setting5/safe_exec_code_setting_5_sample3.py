Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a function that attempts to safely execute Python code by using a restricted execution environment and capturing output. Note that even with these precautions, executing untrusted code is inherently risky and should be avoided if possible.

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


1. **Restricted Environment**: We define a `restricted_globals` dictionary to limit the available built-ins. This helps prevent the execution of potentially dangerous functions.
2. **Output Capture**: We redirect `sys.stdout` to capture any printed output from the executed code.
3. **Error Handling**: We catch exceptions to prevent the function from crashing and return error messages instead.
4. **Security Warning**: Despite these precautions, executing arbitrary code is inherently risky. Consider alternative approaches, such as using a sandboxed environment or a domain-specific language, if possible.