#!/bin/python3

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 44:22:44:22:44:22", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
