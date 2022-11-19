# Imports

import subprocess
import threading
import getopt
import socket
import sys

# Python import bs
sys.path.append('..')


# Global Variables

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

# Defs and all that ig

def usage():
    print ("Angels20 Netcat Replacer")
    print ("")
    print ("Usage: ncatreplacer.py -t target_host -p port")
    print ("-l --listen")
    print ("-e --execute=file_to_run")
    print ("-c --command")
    print ("-u --upload=destination")
    print ("")
    print ("")
    print ("Examples: ")
    print ("")