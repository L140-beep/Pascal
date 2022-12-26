import socket
import struct

class Client():
    
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        
    
    def eval(self, expr : str) -> float:
        bts = expr.encode()
        msglen = len(bts)
        msglen = struct.pack(">h", msglen)
        self.socket.send(msglen)
        self.socket.send(bts)
        result = self.socket.recv(1024)
        
        return result