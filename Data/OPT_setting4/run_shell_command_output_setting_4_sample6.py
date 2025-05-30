To execute a shell command securely in Python using the `subprocess` module, it's crucial to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, pass the command and its arguments as a list. Here's how you can do it:

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

- **Avoid `shell=True`:** This prevents shell injection vulnerabilities.
- **Use `capture_output=True` and `text=True`:** These options capture the output and return it as a string.
- **Handle Exceptions:** Proper error handling ensures the program can gracefully handle unexpected situations.
- **Security Considerations:** Always validate and sanitize input if the command or its arguments are derived from user input to prevent injection attacks.