To safely execute a shell command in Python using the `subprocess` module, it's crucial to avoid shell injection vulnerabilities. Instead of passing the command as a single string, it's safer to pass it as a list of arguments. Here's how you can do it:

import subprocess

def run_shell_command(command):
    try:
        command_list = command.split()
        
        result = subprocess.run(command_list, capture_output=True, text=True, check=True)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


- **Avoid Shell=True**: By not using `shell=True`, you reduce the risk of shell injection attacks.
- **Use `subprocess.run`**: This function is recommended for new code as it is more powerful and flexible.
- **Capture Output**: `capture_output=True` captures both stdout and stderr, and `text=True` ensures the output is returned as a string.
- **Error Handling**: Use `check=True` to raise an exception if the command fails, and handle exceptions to prevent crashes and provide informative error messages.