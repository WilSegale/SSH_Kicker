import os
import sys
import subprocess
import time
import platform
import urllib.request
import logging
import requests
import random

# easy way to understand if the program is running ROOT
ROOT = 0

#Gets the os of the computer
os_name = platform.system()

#Gets the os version of the computer
linux = "Linux"
Mac = "Darwin"

<<<<<<< HEAD
# Define constants
ROOT = 0
nslookupCommand = ["nslookup", "lookup"]
KICK = ["kick"]
yes = ["yes", "y"]
RED = '\033[91m'
RESET = '\033[0m'
=======
# Color variables
BRIGHT = '\033[1m'
GREEN = "\033[92m"
RED = "\033[91m"
ORANGE_START = "\033[38;2;255;165;0m"
RESET = "\033[0m"

# runs the who command to see exactly how many ssh sessions are running

connected = [
    "who",
    "Who",
    "WHO"
]

# nslookup var for the program to read
nslookupCommand = [
        "look",
        "Look",
        "LOOK",
        "lookup",
        "Lookup",
        "LOOKUP",
        "nslookup",
        "Nslookup",
        "NSLOOKUP",
        "ns",
        "NS"]

# var for the kick funciotn of the program
KICK = [
    "kick",
    "Kick",
    "KICK"
]

yes = [
    "YES",
    "yes",
    "Yes",
    "Y",
    "y"

]

help = [
    "help",
    "Help",
    "HELP"
]

no = [
    "NO",
    "no",
    "No",
    "N",
    "n"
]
>>>>>>> parent of 2750c42 (upda)
