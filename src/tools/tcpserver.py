# Import stuff (this gets annoying istg)
import threading
import socket
import sys

# Python bs to import from other places
sys.path.append("..")

# Getting stuff from other files using the append above

from tcpclient import client

# Codey stuff

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Pass IP and port to hear
server.bind((bind_ip, bind_port))

# Listener with 5 backlogs max (you can edit this if you want lol)
server.listen(5)

print("[*] Listening on %s:%d" % bind_ip, bind_port)

# Client-handling stuffles


def handle_client(client_socket):

    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    # Sends back a packet
    client_socket.send("YARR!!")
    client_socket.close()


while True:

    cliet, addr = server.accept()

    print("[*] Accepted connection from: %s%d" % addr[0], addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
