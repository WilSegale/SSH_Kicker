import subprocess
import os
import sys
import datetime
import platform
import time
import urllib.request
import logging
import requests
import random


#Gets the os of the computer
os_name = platform.system()

linux = "Linux"
Mac = "Darwin"

# Color variables
BRIGHT = '\033[1m'
GREEN = "\033[92m"
RED = "\033[91m"
ORANGE_START = "\033[38;2;255;165;0m"
RESET = "\033[0m"

#Easy way to read root form the user
#ROOT = 0

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
    "Yes"
]

no = [
    "NO",
    "no",
    "No"
]