To execute a shell command securely in Python, you should use the `subprocess` module while avoiding shell injection vulnerabilities. It's crucial to avoid passing user input directly to the shell. Instead, use the `subprocess.run` function with a list of arguments. Here's how you can do it:

import subprocess

def run_shell_command(command):
    try:
        args = command.split()
        
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except FileNotFoundError:
        return "Command not found"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


- **Avoid Shell=True**: By not using `shell=True`, you reduce the risk of shell injection attacks.
- **Error Handling**: The function includes error handling for common exceptions, such as `CalledProcessError` and `FileNotFoundError`.
- **Security**: The command is split into a list of arguments to prevent shell injection.
- **Output Capture**: `capture_output=True` captures the command's output, and `text=True` ensures it's returned as a string.