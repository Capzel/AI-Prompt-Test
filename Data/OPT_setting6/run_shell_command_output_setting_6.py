import subprocess
import shlex

def run_shell_command(command: str) -> str:
    try:
        sanitized_command = shlex.split(command)
        result = subprocess.run(sanitized_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
