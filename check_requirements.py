#!/usr/bin/python

import sys, getopt, os
import subprocess
import importlib
import runpy
def main(argv):
    os.system('sudo apt-get update -y')
    os.system('sudo apt-get install python3-dev -y')
    os.system('pip3 install wheel')
    os.system('sudo apt-get install python3-pip python3-setuptools python3-psutil python3-bottle python3-requests python3-dev libzbar-dev libzbar0 -y')
    os.system('sudo pip3 install --upgrade OPi.GPIO')
    os.system('sudo pip3 install ./libraries/SPI-Py')
    os.system('sudo python3 ./libraries/SPI-Py/setup.py install')

if __name__ == "__main__":
   main(sys.argv[1:])