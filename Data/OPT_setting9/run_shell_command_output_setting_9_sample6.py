To safely execute a shell command using Python's `subprocess` module, it's crucial to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, use a list to pass the command and its arguments. Here's how you can do it:

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

- **Security**: By splitting the command into a list, we avoid using `shell=True`, which mitigates the risk of shell injection.
- **Error Handling**: The function handles potential exceptions, such as `CalledProcessError` and `FileNotFoundError`, to ensure robustness.
- **Output Capture**: `capture_output=True` and `text=True` are used to capture and return the command's output as a string.