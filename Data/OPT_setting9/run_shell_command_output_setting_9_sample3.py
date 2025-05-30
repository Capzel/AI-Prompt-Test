To execute a shell command securely using Python's `subprocess` module, it's crucial to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's how you can do it:

import subprocess

def run_shell_command(command):
    try:
        args = command.split()
        
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

output = run_shell_command("ls -l")
print(output)

- **Avoid `shell=True`:** This prevents shell injection vulnerabilities.
- **Use `capture_output=True`:** Captures the output of the command.
- **Use `text=True`:** Ensures the output is returned as a string.
- **Handle exceptions:** Use `try-except` to handle potential errors gracefully.