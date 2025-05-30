import subprocess

def run_shell_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout
    except subprocess.CalledProcessError as error:
        return error.stderr
