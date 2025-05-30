To execute a shell command securely in Python, you should use the `subprocess` module while avoiding the use of `shell=True` to prevent shell injection vulnerabilities. Here's a secure way to run a command and capture its output:

import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True`:** This prevents shell injection vulnerabilities by not invoking the shell.
- **Use a list for the command:** This ensures that each part of the command is treated as a separate argument, which is safer and more reliable.
- **Handle exceptions:** Use `try-except` to catch and handle errors gracefully.
- **Use `capture_output=True`:** This captures the command's output.
- **Use `text=True`:** This ensures the output is returned as a string rather than bytes.