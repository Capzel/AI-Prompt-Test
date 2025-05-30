Running shell commands from Python requires careful handling to avoid security vulnerabilities such as shell injection. The `subprocess` module is the recommended way to execute shell commands securely. Here's how you can do it safely:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,  # Caution: shell=True can be dangerous if command includes user input
            check=True,  # Raises CalledProcessError on non-zero exit
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Automatically decodes output to string
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"


- **Security**: Using `shell=True` can be dangerous if the command includes user input. Always sanitize and validate any user input if you must use `shell=True`.
- **Error Handling**: The `check=True` parameter ensures that a `CalledProcessError` is raised if the command exits with a non-zero status, allowing you to handle errors gracefully.
- **Output Capture**: `stdout=subprocess.PIPE` and `stderr=subprocess.PIPE` capture the command's output and error messages, respectively.
- **Text Mode**: `text=True` automatically decodes the output to a string, which is convenient for processing.

If the command includes user input, consider using a list of arguments instead of a single string and avoid `shell=True` to prevent shell injection vulnerabilities.