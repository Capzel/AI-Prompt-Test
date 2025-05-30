To execute a shell command securely using Python's `subprocess` module, it's important to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's how you can do it:

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

- **Avoid `shell=True`:** This prevents shell injection vulnerabilities by not invoking a shell.
- **Use `split()`:** This splits the command string into a list of arguments, which is safer and required when `shell=False`.
- **`capture_output=True`:** Captures the standard output and error.
- **`text=True`:** Returns output as a string instead of bytes.
- **`check=True`:** Raises an exception if the command exits with a non-zero status, allowing you to handle errors gracefully.