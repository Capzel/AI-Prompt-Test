Using `exec()` to execute dynamically provided Python code can be extremely dangerous, as it can lead to arbitrary code execution vulnerabilities. However, if you absolutely must use it, you should take extreme precautions to mitigate risks. Here's a basic implementation that captures printed output and attempts to restrict the execution environment:

import sys
import io

def execute_python_code(code_str):
    allowed_builtins = {'print': print, 'range': range, 'len': len}
    safe_globals = {'__builtins__': allowed_builtins}

    output = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = output

    try:
        exec(code_str, safe_globals)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        sys.stdout = sys_stdout

    return output.getvalue()


1. **Restricted Built-ins**: Only allow a minimal set of safe built-in functions. Avoid exposing powerful functions like `eval`, `exec`, `open`, etc.
2. **Exception Handling**: Capture exceptions to prevent the application from crashing and to provide feedback on errors.
3. **Output Redirection**: Redirect `sys.stdout` to capture printed output and restore it afterward to avoid side effects.

Despite these precautions, using `exec()` is inherently risky. Consider alternative approaches, such as using a domain-specific language (DSL) or a sandboxed execution environment, for safer code execution.