To execute a shell command securely using Python's `subprocess` module, it's crucial to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's a secure way to do it:

import subprocess

def run_shell_command(command):
    try:
        command_list = command.split()
        
        result = subprocess.run(command_list, capture_output=True, text=True, check=True)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

output = run_shell_command("ls -l")
print(output)

- **Avoid `shell=True`:** This prevents shell injection vulnerabilities.
- **Use `subprocess.run`:** It's a high-level function that provides better control over input/output and error handling.
- **Handle Exceptions:** Use `try-except` to catch and handle errors gracefully.
- **Security:** Always validate and sanitize any user input if the command or its arguments are derived from user input.