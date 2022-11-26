import sys
import os
import subprocess
import platform
import psutil

def get_OS() -> str: #ajouter type d'OS
    print(platform.system())
    print(platform.platform())
    return "test"

def get_CPU() -> str:
    return psutil.cpu_percent()

def get_nom():
    return "test nom"

def get_RAM():
    mem_util = psutil.virtual_memory().percent
    mem_res = psutil.virtual_memory().available
    mem_totale = mem_res + mem_util
    return (mem_util, mem_res, mem_totale)

"""def get_mem_utilisee() -> str:
    return psutil.virtual_memory().percent

def get_mem_restante() -> str:
    return psutil.virtual_memory().available

def get_mem_totale() -> str:
    return 0"""

def get_IP() -> str:
    return 0

def get_hostname() -> str:
    return 0

if __name__=='__main__':
    print(f"OS : {get_OS()}")
    print(f"CPU : {get_CPU()}%")
    print(f"RAM : {get_RAM()}%")

    sys.exit()