Running shell commands from Python requires careful handling to avoid security vulnerabilities such as shell injection. Here's a secure way to execute a shell command using Python's `subprocess` module:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=False, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


1. **Avoid `shell=True`:** Using `shell=True` can expose your code to shell injection vulnerabilities. By passing the command as a list (e.g., `['ls', '-l']`), you avoid this risk.
2. **Error Handling:** The `try-except` block captures and handles exceptions that may occur during command execution.
3. **Security:** By using `subprocess.run()` with `shell=False`, you ensure that the command is executed directly without invoking the shell, which is safer.
4. **Text Mode:** The `text=True` parameter ensures that the output is returned as a string rather than bytes, making it easier to work with in Python 3.

This approach is secure and suitable for running shell commands while minimizing security risks.