Running shell commands from Python requires careful handling to prevent security vulnerabilities, such as command injection. A secure way to execute shell commands is by using Python's `subprocess.run()` method, with proper argument handling. Below is a secure implementation:

import subprocess

def run_shell_command(command):
    if isinstance(command, str):
        raise ValueError("Command must be a list to prevent shell injection.")

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"


- **Argument as List:** Ensure the command is passed as a list of arguments (`List[str]`) to avoid shell injection attacks.
- **`shell=False`:** This prevents the execution from being passed through the shell, another mechanism to mitigate injection risks.
- **Error Handling:** Use `subprocess.CalledProcessError` for handling any execution errors gracefully.
- **Run with Limited Privileges:** Always execute scripts with minimum privileges necessary.

This approach is meant for scenarios where you control the input and can anticipate and handle possible errors securely. If any user input is involved, validation and whitelisting are essential before executing the command.