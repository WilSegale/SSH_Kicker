import subprocess
import os
import sys

# Color variables
BRIGHT = '\033[1m'
GREEN = "\033[92m"
RED = "\033[91m"
ORANGE = "\033[38;2;255;165;0m"
RESET = "\033[0m"

#Easy way to read root form the user
ROOT = 0

# nslookup var for the program to read
nslookupCommand = ["nslookup",
                   "Nslookup",
                   "NSLOOKUP",
                   "ns",
                   "NS"]
# var for the kick funciotn of the program
KICK = ["kick",
        "Kick",
        "KICK"]