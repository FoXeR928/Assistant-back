import socket
from config_init import port_socket

def init_socket():
    server_socket = socket.socket()
    server_socket.bind((socket.gethostname, port_socket))
    server_socket.listen(True)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))