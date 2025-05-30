To execute a shell command securely in Python, you should use the `subprocess` module while avoiding shell injection vulnerabilities. It's crucial to avoid passing user input directly to the shell. Instead, use `subprocess.run()` with a list of arguments. Here's how you can do it:

import subprocess

def run_shell_command(command):
    try:
        args = command.split()
        
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except FileNotFoundError:
        return "Command not found"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

output = run_shell_command("ls -l")
print(output)

- **Avoid Shell=True**: Using `shell=True` can expose your code to shell injection vulnerabilities. Always pass the command as a list of arguments.
- **Error Handling**: Use `try-except` blocks to handle exceptions such as `CalledProcessError` and `FileNotFoundError`.
- **Security**: Ensure that the command and its arguments are validated and sanitized if they originate from user input.
- **Output Capture**: Use `capture_output=True` and `text=True` to capture and return the command's output as a string.