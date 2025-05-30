To execute a shell command securely in Python using the `subprocess` module, it's crucial to avoid using `shell=True` due to the risk of shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's a secure way to run a shell command and return its output:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True`:** This prevents shell injection vulnerabilities.
- **Use `check=True`:** This raises an exception if the command returns a non-zero exit code, allowing you to handle errors gracefully.
- **Use `capture_output=True`:** This captures the command's output, which you can then return or process.
- **Use `text=True`:** This ensures the output is returned as a string rather than bytes.