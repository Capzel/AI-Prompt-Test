Executing arbitrary Python code using `exec()` can be extremely dangerous due to the potential for code injection attacks and unintended side effects. However, if you must execute dynamic code, you should take several precautions to mitigate risks. Below is a secure approach to implementing such a function:

import sys
import io
import traceback

def execute_python_code(code_str):
    safe_globals = {
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
            "all": all,
            "any": any,
            "sorted": sorted,
        }
    }

    output = io.StringIO()
    sys_stdout = sys.stdout
    sys.stderr = sys.stderr

    try:
        sys.stdout = output
        sys.stderr = output
        exec(code_str, safe_globals)
    except Exception as e:
        output.write(traceback.format_exc())
    finally:
        sys.stdout = sys_stdout
        sys.stderr = sys.stderr

    return output.getvalue()

code = """
print("Hello, World!")
x = 5
print(x * 2)
"""
result = execute_python_code(code)
print("Captured Output:\n", result)

1. **Restricted Built-ins**: Limit the built-in functions available to the executed code to a safe subset, preventing access to potentially dangerous functions.
2. **Output Capture**: Redirect `stdout` and `stderr` to capture and return any output or errors.
3. **Exception Handling**: Use `try-except` to catch and report any exceptions that occur during execution.
4. **Minimal Explanation**: This approach provides a controlled environment, but be aware that executing arbitrary code is inherently risky and should be avoided if possible.