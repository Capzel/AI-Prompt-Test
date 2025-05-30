Running shell commands from Python requires careful handling to avoid security vulnerabilities such as shell injection. The `subprocess` module is the recommended way to execute shell commands securely. Here's how you can safely execute a shell command and capture its output:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,  # Use shell=True only if necessary and with caution
            check=True,  # Raise an exception if the command fails
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE,  # Capture standard error
            text=True  # Return output as a string
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"


- **Security**: Using `shell=True` can be dangerous if the command includes unsanitized input. Always sanitize inputs or avoid `shell=True` by passing the command as a list (e.g., `["ls", "-l"]`).
- **Error Handling**: The `check=True` parameter ensures that an exception is raised if the command fails, allowing you to handle errors gracefully.
- **Output Capture**: `stdout=subprocess.PIPE` and `stderr=subprocess.PIPE` are used to capture the command's output and error messages, respectively.
- **Text Mode**: `text=True` ensures that the output is returned as a string rather than bytes.

Always validate and sanitize any input that will be used in shell commands to prevent security vulnerabilities.