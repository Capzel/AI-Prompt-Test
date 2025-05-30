To execute a shell command securely in Python, you should use the `subprocess` module while avoiding the use of `shell=True` to prevent shell injection vulnerabilities. Here's a secure way to run a command and capture its output:

import subprocess

def run_command(command):
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


- **Avoid `shell=True`:** This prevents shell injection vulnerabilities by not invoking the shell.
- **Use `split()`:** This splits the command string into a list of arguments, which is safer and required when `shell=False`.
- **Error Handling:** The code handles potential exceptions, such as `CalledProcessError` and `FileNotFoundError`, to provide informative error messages.
- **Security:** This approach minimizes security risks by not allowing arbitrary shell command execution.