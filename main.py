import unicorn
from app import app
from socket_win import init_socket
from config_init import ip, port_app


if __name__ == "__main__":
    unicorn.run(
        app,
        host=ip,
        port=port_app,
    )
    init_socket()