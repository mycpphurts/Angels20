# Angels20 Netcat Replaces
# Acts like SSH

# Imports

import subprocess
import threading
import getopt
import socket
import sys

# Python import bs
sys.path.append('..')

# Getting vars

from src.var.ncatreplacer.path import listen, command, upload, execute, target, upload_destination, port

# Defs and all that ig


def usage():
    print("Angels20 Netcat Replacer")
    print("")
    print("Usage: ncatreplacer.py -t target_host -p port")
    print("-l --listen")
    print("-e --execute=file_to_run")
    print("-c --command")
    print("-u --upload=destination")
    print("")
    print("")
    print("Examples: ")
    print("ncatreplacer.py -t 192.168.0.1 -p 6969 -l c")
    print("ncatreplacer.py -t 192.168.0.1 -p 1234 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./ncatreplacer.py -t 192.168.11.12 -p 666")
    sys.exit(0)


def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connecting to target host
        client.connect((target, port))

        if len(buffer):
            client.send(buffer)

        while True:
            # Wait for data back
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response+= data

                if recv_len < 4096:
                    break

            print(response),

            # Wait for more input
            buffer = raw_input("")
            buffer += "\n"

            # Send that shit
            client.send(buffer)

    except:
        print("[*] Exception encountered, getting the fuck out")
        client.close()

def server_loop():
    global target

    # Finish this shit next time u open VSC ffs
    # I'm tired as fuck
    # Cybersec is pain istg

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1]):
        usage()

    # Reading CMD options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", [
                                   "help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False,"Unhandled Option"

    

    if not listen and len(target) and port > 0:

        # Read in the buffer from CMD
        # This will block, ***CTRL-D*** if not sending input
        # to stdin
        buffer = sys.stdin.read()

        # Send data OFF
        client_sender(buffer)

        if listen:
            server_loop()

main()