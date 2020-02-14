import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output

def run_shell():
    session = subprocess.Popen(['./api/functions/terraform/terraform.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')