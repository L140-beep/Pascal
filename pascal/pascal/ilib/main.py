from .client import Client
from .server import Server


host = "127.0.0.1"
port = 1489
server = Server(host, port)

server.serve()