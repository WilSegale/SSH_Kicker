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

#Gets the os version of the computer
linux = "Linux"
Mac = "Darwin"

# Define constants

ROOT = 0
nslookupCommand = ["nslookup", "lookup"]
KICK = ["kick"]
connected = ["who"]
no = ["no", "n"]
yes = ["yes", "y"]
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
