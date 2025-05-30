To safely execute a shell command from a string input using Python's `subprocess` module, you should use `subprocess.run()` with appropriate safeguards to avoid security vulnerabilities such as shell injection. Here's how you can do it:

import subprocess
import shlex

def execute_shell_command(command):
    command_args = shlex.split(command)

    try:
        result = subprocess.run(
            command_args,
            capture_output=True,
            text=True,
            check=True
        )
        
        return result.stdout
    
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **`shlex.split(command)`:** Safely parses the command string into a list, ensuring that it's split correctly and handles any special characters securely, reducing injection risk.
- **`subprocess.run()`:** Executes the command with several important parameters:
  - `capture_output=True`: Captures stdout and stderr for processing.
  - `text=True`: Ensures the outputs are returned as strings.
  - `check=True`: Raises a `CalledProcessError` if the command exits with a non-zero status, allowing error handling.
- **Exception Handling:** By catching `subprocess.CalledProcessError`, you can handle errors gracefully.

Avoid using `shell=True` in `subprocess.run()` unless absolutely necessary, as it introduces a security risk when combined with unsanitized input strings.