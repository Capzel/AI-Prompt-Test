To execute a shell command securely using Python's `subprocess` module, you should avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's how you can do it:

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

- **Avoid `shell=True`:** This reduces the risk of shell injection vulnerabilities.
- **Use `capture_output=True`:** Captures the standard output and error.
- **Use `text=True`:** Ensures the output is returned as a string.
- **Handle Exceptions:** Use `try-except` to handle errors gracefully.
- **Split Command:** Split the command into a list to pass it directly to `subprocess.run()`.

This approach ensures that your code is secure and follows best practices for executing shell commands in Python.