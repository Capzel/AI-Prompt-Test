import subprocess

def run_shell_command(user_command):
    process = subprocess.Popen(user_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    return stdout, stderr, process.returncode