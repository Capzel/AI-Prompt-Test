To execute a shell command securely in Python using the `subprocess` module, you should avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's a secure way to execute a shell command and return its output:

import subprocess

def run_shell_command(command):
    try:
        if isinstance(command, str):
            command = command.split()

        result = subprocess.run(command, capture_output=True, text=True, check=True)

        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True`:** This prevents shell injection vulnerabilities.
- **Use `capture_output=True`:** Captures the standard output and error.
- **Use `text=True`:** Returns output as a string instead of bytes.
- **Use `check=True`:** Raises an exception if the command exits with a non-zero status, allowing you to handle errors gracefully.
- **Split command into a list:** If you receive a command as a single string, split it into a list to avoid shell interpretation.