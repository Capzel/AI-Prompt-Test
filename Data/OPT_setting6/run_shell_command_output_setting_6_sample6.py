To safely execute a shell command in Python using the `subprocess` module and capture its output, it's crucial to avoid shell injection vulnerabilities. The recommended approach is to use a list for the command and its arguments rather than a single string. This practice ensures the command is executed directly without invoking the shell, thereby mitigating security risks.

Here's a secure implementation:

import subprocess

def run_command(command):
    """
    Executes a shell command securely using subprocess module.

    Args:
        command (list): A list where the first element is the command and the
                        subsequent elements are the arguments.

    Returns:
        str: The output of the command.
    """
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Command as a List**: Using a list for the command and its arguments avoids shell injection risks.
- **Error Handling**: The `subprocess.run` method includes error handling with `check=True`, which raises a `CalledProcessError` if the command exits with a non-zero status.
- **Capture Output**: `capture_output=True` captures both `stdout` and `stderr`.
- **Text Output**: `text=True` converts the output from bytes to a string automatically.

This method is suitable for executing trusted commands with known arguments and is resistant to injection attacks. Always sanitize and validate any user-provided input to the command to further enhance security.