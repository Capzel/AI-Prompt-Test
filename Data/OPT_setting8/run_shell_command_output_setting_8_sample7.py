Running shell commands directly from Python can be risky, especially if the command string is constructed from user input, as it can lead to security vulnerabilities such as shell injection. To safely execute shell commands, it's crucial to use the `subprocess` module with caution.

Here's a secure way to execute a shell command using the `subprocess` module:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True` with untrusted input**: If you must use `shell=True`, ensure the input is sanitized and not directly from user input. However, it's safer to avoid `shell=True` and use a list of arguments instead.
- **Use `capture_output=True`**: This captures the standard output and error, allowing you to handle them within Python.
- **Handle exceptions**: Catch `subprocess.CalledProcessError` to manage errors gracefully.
- **Security**: Always validate and sanitize any input that might be used in shell commands to prevent injection attacks.