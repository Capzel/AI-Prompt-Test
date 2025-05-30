Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you must use it, you should take several precautions to mitigate risks. Below is a function that attempts to safely execute Python code by using a restricted execution environment and capturing output:

import sys
import io

def execute_python_code(code_str):
    restricted_globals = {
        "__builtins__": {
            "print": print,
            "range": range,
            "len": len,
            "int": int,
            "float": float,
            "str": str,
            "bool": bool,
            "list": list,
            "dict": dict,
            "set": set,
            "tuple": tuple,
            "enumerate": enumerate,
            "zip": zip,
            "map": map,
            "filter": filter,
            "sum": sum,
            "min": min,
            "max": max,
            "abs": abs,
        }
    }
    
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    try:
        exec(code_str, restricted_globals)
        output = sys.stdout.getvalue()
    except Exception as e:
        output = f"Error: {e}"
    finally:
        sys.stdout = old_stdout
    
    return output

code = """
for i in range(3):
    print(i)
"""
print(execute_python_code(code))

1. **Restricted Environment**: The `restricted_globals` dictionary limits the available built-in functions to a safe subset. This helps prevent the execution of potentially dangerous functions.
2. **Output Capture**: Redirects `sys.stdout` to capture any printed output from the executed code.
3. **Error Handling**: Catches exceptions to prevent the application from crashing and returns error messages safely.
4. **Minimal Built-ins**: Only includes a minimal set of safe built-in functions. You should carefully evaluate which functions are necessary and safe for your use case.

Despite these precautions, using `exec()` is inherently risky, and it's generally better to avoid executing arbitrary code strings whenever possible. Consider alternative approaches, such as using a domain-specific language (DSL) or a sandboxed environment, for executing untrusted code.