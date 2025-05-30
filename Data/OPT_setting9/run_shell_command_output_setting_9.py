import subprocess
import shlex

def run_shell_command(command: str) -> str:
    safe_command = shlex.split(command)
    try:
        result = subprocess.run(
            safe_command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"