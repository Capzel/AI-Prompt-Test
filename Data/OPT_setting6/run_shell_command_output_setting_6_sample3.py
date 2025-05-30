To execute a shell command securely using Python's `subprocess` module, it's crucial to avoid using `shell=True` to prevent shell injection vulnerabilities. Instead, split the command into a list of arguments. Here is how you can implement this:

import subprocess

def run_command(command: str) -> str:
    args = command.split()
    
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except FileNotFoundError:
        return "Command not found"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


- **Avoid `shell=True`:** Directly using `shell=True` can expose your application to shell injection vulnerabilities.
- **Split Command into List:** This ensures each part of the command is treated as an individual argument.
- **Handle Exceptions:** Use `try-except` blocks to handle potential exceptions like `CalledProcessError` and `FileNotFoundError` to make the code robust.
- **Capture Output:** Use `capture_output=True` and `text=True` to capture and return the output as a string.
- **Use `check=True`:** Ensures that an exception is raised for non-zero exit codes, allowing you to handle errors gracefully.