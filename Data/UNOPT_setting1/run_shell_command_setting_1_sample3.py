import subprocess

def run_shell_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout