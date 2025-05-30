To safely run a shell command using Python's `subprocess` module, it is recommended to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command as a list of arguments where possible. Here's how you can safely implement this:

import subprocess
from shlex import split

def run_shell_command(command):
    try:
        args = split(command)
        
        result = subprocess.run(args, check=True, text=True, capture_output=True)
         
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except FileNotFoundError:
        return "Command not found."

output = run_shell_command("ls -la")
print(output)


1. **Shell Injection Prevention**: By not using `shell=True` and splitting the command string into arguments with `shlex.split`, we significantly reduce the risk of shell injection.

2. **Error Handling**: The `try-except` block is used to catch and handle exceptions such as `CalledProcessError` when a command fails (e.g., non-zero exit status) and `FileNotFoundError` when the command is not recognized.

3. **Portability**: This method enhances portability as argument splitting provides a way to correctly parse command-line arguments across different platforms.

Using `subprocess.run()` is both safe and powerful when working with external commands and affords better control over input/output streams and errors when compared to older methods like `os.system()`.