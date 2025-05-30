To safely execute a shell command in Python using the `subprocess` module, it's crucial to avoid security risks such as shell injection. Here's how you can do it securely:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


1. **Avoid `shell=True` with untrusted input**: Using `shell=True` can be dangerous if the command is constructed from untrusted input. In this example, it's assumed that the input is trusted. If not, avoid `shell=True` and pass the command as a list of arguments.

2. **Use `subprocess.run`**: This is the recommended approach for running subprocesses as it provides more control and better error handling.

3. **Capture Output**: `capture_output=True` captures the command's output, and `text=True` ensures the output is returned as a string.

4. **Error Handling**: The `check=True` parameter ensures that an exception is raised if the command returns a non-zero exit status, allowing you to handle errors gracefully.

Always validate and sanitize any input that could be used to construct shell commands to prevent injection vulnerabilities.