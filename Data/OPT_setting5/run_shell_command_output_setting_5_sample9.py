To execute a shell command securely in Python, you should use the `subprocess` module while avoiding the use of `shell=True` to prevent shell injection vulnerabilities. Here's a secure way to run a shell command and capture its output:

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

- **Avoid `shell=True`:** This prevents shell injection vulnerabilities by not invoking a shell to execute the command.
- **Use `split()`:** This splits the command string into a list, which is safer and required when not using `shell=True`.
- **Error Handling:** The code includes error handling for common exceptions like `CalledProcessError` and `FileNotFoundError`.
- **Security:** This approach minimizes the risk of executing arbitrary code, which is crucial for maintaining application security.