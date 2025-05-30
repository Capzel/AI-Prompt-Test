import subprocess
import shlex

def run_shell_command(command: str) -> str:
    safe_command = shlex.split(command)
    result = subprocess.run(safe_command, capture_output=True, text=True, check=True)
    return result.stdout
