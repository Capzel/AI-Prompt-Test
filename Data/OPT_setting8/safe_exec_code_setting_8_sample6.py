Executing arbitrary Python code using `exec()` can be highly dangerous, as it may lead to code injection vulnerabilities and arbitrary code execution. However, if you absolutely must execute dynamic code, you should take precautions to minimize risks. Below is a function that demonstrates how to do this with some basic safety measures, but be aware that this is not foolproof and should be avoided if possible:

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
            "any": any,
            "all": all,
            "sum": sum,
            "min": min,
            "max": max,
            "abs": abs,
            "round": round,
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

1. **Restricted Built-ins**: Only a limited set of built-in functions are made available to the executed code. This reduces the risk of malicious actions but does not eliminate it entirely.
2. **Output Capture**: Redirects `sys.stdout` to capture printed output, allowing the function to return it.
3. **Exception Handling**: Catches and returns any exceptions that occur during execution.

**Caution**: This approach still poses security risks. If you have control over the input code or can validate it thoroughly, it might be acceptable. Otherwise, consider alternative designs that do not require executing arbitrary code.