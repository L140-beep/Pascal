import socket
import threading
import time
import struct
from .interpreter import Interpreter, InterpreterException

class Server:

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._clients = []

    def _process_client(self, conn, addr):
        with conn:
            data = b''
            interp = Interpreter()
            while True:
                try:
                    bts = conn.recv(2)
                    msglen = struct.unpack(">h", bts)[0]
                    data = conn.recv(msglen)
                    try:
                        result = interp.eval(data.decode())
                        conn.sendall(str(result).encode())
                    except InterpreterException as e:
                        conn.sendall(str(e).encode())
                except BlockingIOError:
                    time.sleep(0.2)
                    continue
                if not data:
                    break
        print(f"Client socket closed {addr}")

    def serve(self):
        with socket.socket(socket.AF_INET, 
                    socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET,
                            socket.SO_REUSEADDR, 1)
            sock.bind((self._host, self._port))
            sock.setblocking(False)
            sock.listen(3)
            threads = []
            while True:
                try:
                    conn, addr = sock.accept()
                    print(f"New client accepted {addr}")
                    t = threading.Thread(target=self._process_client, args=(conn, addr))
                    t.start()
                    threads.append(t)
                    for th in threads[:]:
                        if not th.is_alive():
                            threads.remove(th)
                    print(f"Client threads = {len(threads)}")
                except BlockingIOError:
                    time.sleep(0.2)
