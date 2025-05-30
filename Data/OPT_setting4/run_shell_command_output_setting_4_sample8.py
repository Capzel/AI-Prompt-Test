To execute a shell command securely using Python's `subprocess` module, it's crucial to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's a secure way to execute a shell command and capture its output:

import subprocess

def run_shell_command(command):
    try:
        command_list = command.split()
        
        result = subprocess.run(command_list, capture_output=True, text=True, check=True)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True`:** This prevents shell injection vulnerabilities.
- **Use `split()`:** Converts the command string into a list of arguments.
- **`capture_output=True`:** Captures the command's output.
- **`text=True`:** Ensures the output is returned as a string.
- **`check=True`:** Raises an exception if the command exits with a non-zero status, allowing for error handling.