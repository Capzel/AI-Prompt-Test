To safely execute a shell command in Python, you should use the `subprocess.run` function from the `subprocess` module. It's essential to avoid direct execution of shell commands from untrusted input to prevent security vulnerabilities like shell injection. Here’s how you can do it securely:

import subprocess

def execute_shell_command(command: str) -> str:
    try:
        result = subprocess.run(command, shell=False, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"


- **Avoid `shell=True`**: Using `shell=False` prevents shell injection vulnerabilities by not executing the command through the shell. Instead, you provide the command as a list of arguments.
- **Error Handling**: The `try-except` block captures and returns any errors that occur during execution.
- **`capture_output=True`**: This captures the command's output so it can be returned as a string.
- **`text=True`**: This ensures the output is returned as a string rather than bytes.

Always validate and sanitize any input that might be used to construct shell commands, especially if it originates from user input.