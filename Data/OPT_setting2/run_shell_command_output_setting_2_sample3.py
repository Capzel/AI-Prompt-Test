To execute a shell command securely in Python, you should use the `subprocess` module while avoiding the use of `shell=True` to prevent shell injection vulnerabilities. Here's a secure way to run a shell command and capture its output:

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

- **Avoid `shell=True`:** This prevents shell injection vulnerabilities by not invoking the shell.
- **Use `split()`:** This splits the command string into a list, which is safer for `subprocess.run`.
- **Error Handling:** Includes handling for `CalledProcessError`, `FileNotFoundError`, and other exceptions to ensure robustness.
- **`capture_output=True`:** Captures the command's output.
- **`text=True`:** Ensures the output is returned as a string rather than bytes.