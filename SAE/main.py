import sys
import os
import subprocess
import platform
import psutil

def get_OS_() -> str:
    return platform.system()

def get_CPU() -> str:
    return psutil.cpu_percent()

def get_mem_utilisee() -> str:
    return psutil.virtual_memory().percent

def get_mem_restante() -> str:
    return psutil.virtual_memory().available

def get_mem_totale() -> str:
    return 0

def get_IP() -> str:
    return 0

def get_hostname() -> str:
    return 0

if __name__=='__main__':
    print(f"OS : {get_OS_()}")
    print(f"CPU : {get_CPU()}%")
    print(f"mémoire utilisée : {get_mem_utilisee()}%")
    print(f"mémoire restante : {get_mem_restante()}")

    sys.exit()