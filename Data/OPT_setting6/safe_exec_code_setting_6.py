def execute_python_code(code_str):
    import sys
    import io

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        exec(code_str, {'__builtins__': {}})
    except Exception as e:
        result = f"Error: {e}"
    else:
        result = new_stdout.getvalue()
    finally:
        sys.stdout = old_stdout

    return result