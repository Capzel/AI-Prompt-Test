import subprocess

def run_shell_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return {'stdout': result.stdout, 'stderr': result.stderr, 'returncode': result.returncode}