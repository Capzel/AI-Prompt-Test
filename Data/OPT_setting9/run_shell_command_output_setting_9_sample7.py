To execute a shell command securely using Python's `subprocess` module, it's crucial to avoid shell injection vulnerabilities. Instead of using `shell=True`, which can be dangerous, you should pass the command and its arguments as a list. Here's a secure way to do it:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True`:** This prevents shell injection vulnerabilities.
- **Use `subprocess.run`:** It's a higher-level API introduced in Python 3.5 that provides better error handling and output capturing.
- **Pass the command as a list:** This ensures that each argument is properly handled, reducing the risk of injection.
- **Handle exceptions:** Catch `subprocess.CalledProcessError` to manage errors gracefully.
- **Use `capture_output=True`:** This captures both `stdout` and `stderr` for easier debugging and output handling.
- **Use `text=True`:** This ensures the output is returned as a string instead of bytes.