import sys
import os
import subprocess

class Fonctionnalites:
    def __init__(self):
        test = 1

    def get_OS(self):
        cmd = "ping -c 3 8.8.8.8"
        shellcmd = os.popen(cmd)
        print(shellcmd.read())
        cmd = ['ping', '-c', '3', '8.8.8.8']
        shell_cmd = subprocess.run((cmd))
        print(shell_cmd)

def get_OS():
     cmd = "ping 8.8.8.8"
     shellcmd = os.popen(cmd)
     print(shellcmd.read())
     """cmd = ['ping', '8.8.8.8']
     shell_cmd = subprocess.run((cmd))
     print(shell_cmd)"""
def get_OS_():
    os.system()
    cmd = ['ping', '8.8.8.8']
    shell_cmd = subprocess.run((cmd), capture_output=True, text=True)
    command_output = (shell_cmd.stdout)
    print(command_output)


if __name__=='__main__':
    os.system("ping 8.8.8.8")
    os.system()
    #os.name
    #print(os.uname())
    """get_OS()
    get_OS_()"""
    sys.exit()