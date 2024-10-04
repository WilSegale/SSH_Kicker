import os
import sys
import subprocess
import time
import platform
import urllib.request
import logging
import requests
import random


#Gets the os of the computer
os_name = platform.system()

linux = "Linux"
Mac = "Darwin"
windows = "Windows"


# Define constants
ROOT = 0
nslookupCommand = ["nslookup", "lookup"]
KICK = ["kick"]
yes = ["yes", "y"]
RED = '\033[91m'
RESET = '\033[0m'
