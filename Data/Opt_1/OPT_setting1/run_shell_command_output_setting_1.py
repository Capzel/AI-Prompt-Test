import subprocess
import shlex

def execute_command(command: str) -> str:
    safe_command = shlex.split(command)
    result = subprocess.run(safe_command, capture_output=True, text=True, check=False)
    return result.stdout