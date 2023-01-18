import os, subprocess
def name():
    print(subprocess.check_output(["/home/ward/Downloads/test3/gpu-utils getname"], stderr=subprocess.STDOUT, shell=True))
def printer():
    print(0)
printer()
name()
