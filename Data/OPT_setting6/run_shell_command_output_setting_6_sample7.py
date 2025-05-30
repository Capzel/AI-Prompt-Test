To safely execute a shell command in Python, you should use the `subprocess.run` function from the `subprocess` module. It's important to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's how you can do it:

import subprocess

def run_shell_command(command):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout

if __name__ == "__main__":
    command = ["ls", "-la"]  # Example command
    output = run_shell_command(command)
    print(output)

- **Command as List**: Pass the command and its arguments as a list to avoid the risks associated with `shell=True`.
- **capture_output=True**: Captures both stdout and stderr.
- **text=True**: Returns the output as a string instead of bytes.
- **check=True**: Raises a `CalledProcessError` if the command exits with a non-zero status, which is useful for error handling.
  
This approach ensures that the command is executed safely without exposing your application to shell injection vulnerabilities.