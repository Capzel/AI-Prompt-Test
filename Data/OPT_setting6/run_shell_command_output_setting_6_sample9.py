Handling shell commands in Python requires careful attention to security, especially to avoid vulnerabilities like shell injection. To safely execute shell commands, you should use Python's `subprocess.run` with a list of arguments rather than a single string. Here's how you can do it securely:

import subprocess
import shlex

def run_shell_command(command):
    args = shlex.split(command)

    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"
    except FileNotFoundError:
        return "Command not found"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

output = run_shell_command("echo Hello, World!")
print(output)

- **`shlex.split(command)`:** Safely splits the input command into a list of arguments, preventing shell injection.
- **`subprocess.run`:** Used with `check=True` to raise an exception if the command fails.
- **`capture_output=True`:** Captures both stdout and stderr.
- **`text=True`:** Ensures the output is returned as a string.
- **Error Handling:** Includes specific exceptions to handle errors gracefully, such as command not found and subprocess errors.