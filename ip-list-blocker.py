#!/usr/bin/env python

# Written by: Syntax
# Twitter: @CockSlime

import subprocess, sys, os
from time import sleep

# Check for blacklist argument
if len(sys.argv) != 2:
    print("\nUsage: \x1b[35m"+sys.argv[0]+" \x1b[37m[\x1b[35mblacklist-file\x1b[37m]\x1b[0m")
    print("\x1b[37mMade by Syntax.\x1b[0m")
    print("\x1b[35;1mhttps://github.com/cannabispowered\x1b[0m\n")
    sys.exit(0)

# Check for `iptables`
if not os.path.exists("/sbin/iptables"):
    sys.exit("\x1b[31;1mError: Unable to locate the iptables binary.\x1b[0m\n")

# Check existance of supplied blacklist file.
listInput = sys.argv[1]
if not os.path.exists(sys.argv[1]):
    sys.exit("\x1b[31;1mError: File \"%s\" not found.\x1b[0m\n" % listInput)

# Open blacklist file 
file = open(listInput, "r")
lines = file.readlines()

def beginBlacklist():
    print "\x1b[35;1mBlacklisting will begin in 5 seconds.\x1b[0m"
    sleep(5)
    print "\x1b[35;1mBlacklisting has now begun. This may take a moment, please be patient.\x1b[0m"

    try:
        for line in lines:
            command = "iptables -A INPUT -s %s -j DROP" % line.rstrip('\n')
            subprocess.call(command,shell=True)

            command = "iptables -A OUTPUT -s %s -j DROP" % line.rstrip('\n')
            subprocess.call(command,shell=True)

            command = "iptables -A FORWARD -s %s -j DROP" % line.rstrip('\n')
            subprocess.call(command,shell=True)

        sys.exit("\x1b[32;1mEach line in "+listInput+" has been blacklisted!\x1b[0m")
    except KeyboardInterrupt:
        sys.exit("\n\x1b[31;1mCaught SIGINT(CTRL+C). Exiting.\x1b[0m")

# Initalize
beginBlacklist()
