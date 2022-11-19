# Imports

import subprocess
import threading
import getopt
import socket
import sys

# Variables for ./src/tools/ncatreplacer.py

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0