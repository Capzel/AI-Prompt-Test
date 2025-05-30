Using `exec()` to execute dynamically provided Python code can be highly dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take extreme precautions. Below is a minimal implementation that attempts to mitigate some risks by using a restricted execution environment. Note that even with these precautions, executing arbitrary code is inherently risky and should be avoided if possible.

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

code = """
print("Hello, World!")
"""
print(execute_python_code(code))

1. **Restricted Environment**: We define a restricted set of built-in functions that are safe to use. This limits what the executed code can do.
2. **Output Capture**: We redirect `sys.stdout` to capture any printed output, which is then returned.
3. **Error Handling**: We catch exceptions to prevent the application from crashing and to provide feedback on errors.
4. **Security Warning**: Despite these precautions, executing arbitrary code remains risky. Consider safer alternatives, such as using a domain-specific language or a sandboxed execution environment.