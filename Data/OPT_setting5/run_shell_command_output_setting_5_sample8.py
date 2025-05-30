To execute a shell command securely in Python using the `subprocess` module, it's crucial to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's a secure way to do it:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True`:** This prevents shell injection vulnerabilities.
- **Use `capture_output=True`:** Captures the command's output.
- **Use `text=True`:** Returns output as a string instead of bytes.
- **Handle exceptions:** Use `try-except` to catch and handle errors gracefully.