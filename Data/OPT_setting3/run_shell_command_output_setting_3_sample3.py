To execute a shell command securely in Python, you should use the `subprocess` module while avoiding shell injection vulnerabilities. It's crucial to avoid passing user input directly to the shell. Instead, use a list to specify the command and its arguments. Here's a secure way to do it:

import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid Shell=True**: Using `shell=True` can expose your code to shell injection vulnerabilities. By passing the command as a list, you mitigate this risk.
- **Error Handling**: The `try-except` block captures any errors that occur during command execution, providing a safe way to handle exceptions.
- **Security**: Always validate and sanitize any user input if it must be included in the command arguments.