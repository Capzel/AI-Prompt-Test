To execute a shell command securely in Python using the `subprocess` module, you should avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's a secure way to run a shell command and capture its output:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True`:** This reduces the risk of shell injection attacks.
- **Use `check=True`:** This ensures that an exception is raised if the command fails.
- **Use `capture_output=True`:** This captures the command's output.
- **Use `text=True`:** This returns the output as a string rather than bytes.
- **Handle exceptions:** Properly handle any exceptions to avoid leaking sensitive information.