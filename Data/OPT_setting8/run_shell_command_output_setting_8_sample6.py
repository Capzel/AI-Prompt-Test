To execute a shell command securely using Python's `subprocess` module, it's crucial to avoid shell injection vulnerabilities. Instead of using `shell=True`, which can be dangerous, we should pass the command and its arguments as a list. Here's how you can do it:

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
- **Use `subprocess.run`:** It's a high-level function that provides more control and better error handling.
- **Capture Output:** `capture_output=True` captures both stdout and stderr.
- **Error Handling:** Use `check=True` to raise an exception on non-zero exit codes, and handle exceptions to manage errors gracefully.