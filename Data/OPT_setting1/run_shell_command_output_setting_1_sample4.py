Using Python's `subprocess` module to execute shell commands should be approached with extreme caution, particularly when dealing with untrusted input, to prevent security vulnerabilities such as shell injection. The example provided below adheres to secure practices by avoiding the use of `shell=True` and employing `shlex.split()` to safely parse the command:

import subprocess
import shlex

def run_shell_command(command: str) -> str:
    args = shlex.split(command)
    
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

- **No `shell=True`:** Avoids `shell=True` for security to prevent shell injection risks.
- **`shlex.split()`:** Uses `shlex.split()` to safely handle shell syntax from the input command string while preserving argument separation.
- **Error Handling:** Catches exceptions like `subprocess.CalledProcessError` to manage errors gracefully.
  
This method provides a safer alternative when executing shell commands from user input. However, always validate and sanitize input if it arises from untrusted sources.