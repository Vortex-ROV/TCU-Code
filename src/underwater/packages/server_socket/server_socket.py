import socket


class ServerSocket:
    # closed = 0  #try it 29/4/2024 if not working remove it 
    def __init__(self, port: int = 12345, address: str = "192.168.33.1"):
        self.__welcoming_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__welcoming_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__welcoming_socket.bind((address, port))
        self.__welcoming_socket.listen()

    def accept(self):
        # self.closed=1 #try it 29/4/2024 if not working remove it 
        print("waiting for client")
        self.__client_socket, _ = self.__welcoming_socket.accept()
        self.__client_socket.setblocking(False)
        # self.closed=0  #try it 29/4/2024 if not working remove it 
        print("connected to client")

    def receive(self, buffer_size: int):
        try:
            received = self.__client_socket.recv(buffer_size).decode()
            if received is not None and len(received) != 0:
                return received
            raise socket.error
        except socket.error as e:
            # handle receive not ready
            if e.errno == 11:
                return
            print(e)
            self.__client_socket.close()
            self.accept()

    def send(self, data: bytes):
        try:
            self.__client_socket.send(data)
        except socket.error as e:
            if e.errno == 10035:
                return
            print(e)
            self.__client_socket.close()
            self.accept()
        except AttributeError as e:
            pass
    # def closedSocket(self): #try it 29/4/2024 if not working remove it / to handle if socket disconnected stop rov until its connected again 
    #     return self.closed


if __name__ == "__main__":
    sock = ServerSocket(12345, "localhost")
    sock.accept()

    while True:
        sock.send(("0" * 48 + "021").encode())
