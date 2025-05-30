import subprocess

def run_shell_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    returncode = process.returncode
    return returncode, stdout, stderr