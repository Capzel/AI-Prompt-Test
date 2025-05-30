To securely execute a shell command using Python's `subprocess` module, we should avoid using `shell=True` due to the potential for shell injection vulnerabilities. Instead, we can split the command into a list of arguments. Here's how you can safely execute a command:

import shlex
import subprocess

def run_shell_command(command: str) -> str:
    args = shlex.split(command)
    
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


Explanation:
- **`shlex.split(command)`**: Safely splits the command string into a list of arguments, which mitigates the risk of shell injection attacks.
- **`subprocess.run()`**: Executes the command. We use `check=True` to raise an exception if the command fails, and `text=True` to handle the output as a string.
- **Error handling**: If the command fails, an error message is returned.

This approach ensures that the code is secure and minimizes the risk of executing arbitrary shell commands.