import subprocess

def run_shell_command(command: str) -> str:
    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    return result.stdout.strip()