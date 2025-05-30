To execute a shell command securely in Python, you should use the `subprocess` module but avoid using functions that are vulnerable to shell injection, such as `subprocess.run` with `shell=True`. Instead, use a list to specify the command and its arguments, which helps mitigate the risk of shell injection.

Here's how you can safely execute a shell command and return its output as a string:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **List Arguments:** The command is passed as a list of arguments (e.g., `["ls", "-l"]`). This prevents shell injection vulnerabilities because it does not invoke a shell to parse the command.
- **`check=True`:** This raises a `CalledProcessError` if the command exits with a non-zero status, allowing you to handle errors gracefully.
- **`capture_output=True`:** Captures both stdout and stderr.
- **`text=True`:** Ensures the output is returned as a string rather than bytes.

This approach ensures that the subprocess is executed securely and that the output is returned in a safe and controlled manner.