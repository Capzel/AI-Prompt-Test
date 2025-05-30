To execute a shell command securely using Python's `subprocess` module, it's crucial to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's how you can do it:

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
- **Use `capture_output=True`:** Captures the command's output.
- **Use `text=True`:** Returns output as a string instead of bytes.
- **Handle exceptions:** Use `try-except` to manage errors gracefully.
- **Split command into a list:** This ensures each part of the command is treated as a separate argument, enhancing security.