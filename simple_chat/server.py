import concurrent.futures
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import logging
from concurrent.futures import ThreadPoolExecutor
import datetime

class ChatServer:

    def __init__(self, host, port):
        self.logger = self._setup_logger()
        self.sock = self._setup_socket(host, port)
        self.connections = []


    def run(self):
        self.logger.info('Chat server is running')
        with ThreadPoolExecutor() as executor:
            while True:
                conn, addr = self.sock.accept()
                self.logger.debug(f'New connection: {addr}')

                self.connections.append(conn)
                self.logger.debug(f"Conections: {self.connections}")

                executor.submit(self.relay_messages, conn, addr)


    def relay_messages(self, conn, addr):
        while True:
            data = conn.recv(4096)

            for connection in self.connections:
                a = str(addr[0] + " | ").encode('utf-8')
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                now += " | "
                now = now.encode('utf-8')
                connection.send(a + now + data)

            if not data:
                self.logger.warning("No data. Exiting. ")
                break


    @staticmethod
    def _setup_socket(host, port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen()
        return sock


    @staticmethod
    def _setup_logger():
        logger = logging.getLogger('chat_server')
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        return logger

if __name__ == "__main__":
    from simple_chat.settings import SERVER_HOST, SERVER_PORT
    server = ChatServer(SERVER_HOST, SERVER_PORT)
    server.run()