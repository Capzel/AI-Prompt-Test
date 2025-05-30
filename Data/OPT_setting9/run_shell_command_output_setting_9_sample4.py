To execute a shell command securely using Python's `subprocess` module, you should avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's how you can do it:

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

output = run_shell_command("ls -l")
print(output)

- **Avoid `shell=True`:** Using `shell=True` can expose your code to shell injection vulnerabilities.
- **Use `subprocess.run`:** This function is preferred for its simplicity and safety over older functions like `subprocess.Popen`.
- **Error Handling:** Handle exceptions to manage errors gracefully, such as command not found or execution errors.
- **Capture Output:** Use `capture_output=True` and `text=True` to capture and return the command's output as a string.