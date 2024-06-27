from socket import socket, AF_INET, SOCK_STREAM
import logging

class ChatServer:
    
    def __init__(self, host, port):
        self.logger = self._setup_logger()
        self.sock = self._setup_socket(host, port)


    def run(self):
        self.logger.info('Chat server is running')
        
        while True:
            conn, addr = self.sock.accept()
            self.logger.debug(f'New connection: {addr}')

    
    @staticmethod
    def _setup_socket(host, port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind((host, port))
        sock.listen()
        return sock
    

    @staticmethod
    def _setup_logger():
        logger = logging.getLogger('chat_server')
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(logging.DEBUG)
        return logger
            