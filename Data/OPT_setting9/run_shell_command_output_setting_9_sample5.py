To execute a shell command securely using Python's `subprocess` module, it's crucial to avoid using `shell=True` due to the risk of shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's a secure way to implement this:

import subprocess

def run_shell_command(command):
    try:
        command_list = command.split()
        
        result = subprocess.run(command_list, capture_output=True, text=True, check=True)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except FileNotFoundError:
        return "Command not found"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

output = run_shell_command("ls -l")
print(output)

- **Avoid `shell=True`:** This prevents shell injection vulnerabilities by not invoking a shell to interpret the command.
- **Use `capture_output=True`:** Captures the standard output and error.
- **Use `text=True`:** Ensures the output is returned as a string rather than bytes.
- **Error Handling:** Includes handling for `CalledProcessError`, `FileNotFoundError`, and general exceptions to provide informative error messages.
- **Command Splitting:** The command is split into a list to safely pass it to `subprocess.run()`. This is crucial for security and correctness.