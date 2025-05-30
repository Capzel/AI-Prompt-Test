import subprocess
import shlex

def run_shell_command(command: str) -> str:
    try:
        safe_command = shlex.split(command)
        result = subprocess.run(safe_command, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"