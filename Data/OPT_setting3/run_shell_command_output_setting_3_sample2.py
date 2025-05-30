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
- **Use `subprocess.run`:** It's a higher-level API that is more secure and easier to use.
- **Handle Exceptions:** Use `try-except` to catch and handle errors gracefully.
- **Capture Output:** Use `capture_output=True` and `text=True` to get the output as a string.
- **Check for Errors:** `check=True` raises an exception if the command returns a non-zero exit code.