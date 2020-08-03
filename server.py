import selectors
import sys
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM,
    SOL_SOCKET,
    SO_REUSEADDR
    )

from common.variables import (
    MAX_SIZE_RECEIVE_DATA,
    DEFAULT_ENCODING,
    DEFAULT_ADDR,
    DEFAULT_PORT
    )
from common.utils import (
    args_validation,
    get_args
    )

from common.metaclass import ServerVerifier
from common.descriptor import (
    PortVerifier,
    AddrVerifier
    )
from common.decorators import LogInfo


class Server(metaclass=ServerVerifier):
    server_socket = socket(AF_INET, SOCK_STREAM)
    clients = {}
    _port = PortVerifier()
    _addr = AddrVerifier()

    selector = selectors.DefaultSelector()

    @LogInfo('full')
    def __init__(self, addr, port):
        self.server_socket.setsockopt(
            SOL_SOCKET,
            SO_REUSEADDR,
            1)
        
        self._port = port
        self._addr = addr
        if not self._port or not self._addr:
            sys.exit(1)

        self.server_socket.bind((self._addr, self._port))
        self.server_socket.listen()
        print('Server started!')

        self.selector.register(
            fileobj=self.server_socket,
            events=selectors.EVENT_READ,
            data=self.accept_connection
            )

    @LogInfo('full')
    def accept_connection(self, server_socket):
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)

        if client_socket not in self.clients:
            client_socket.send('GET_NICK'.encode(DEFAULT_ENCODING))
            nike_name = client_socket.recv(MAX_SIZE_RECEIVE_DATA).decode(DEFAULT_ENCODING)
            self.clients[client_socket] = nike_name

            self.broadcast(f'{nike_name} is joined!\n', client_socket)
            client_socket.send('Welcom to server chat!'.encode(DEFAULT_ENCODING))
            client_socket.send(
                '\n1) To send messages to a shared chat, type it and press "Enter"'.encode(DEFAULT_ENCODING)
                )
            client_socket.send(
                '\n2) For a private message, type the user name and the message "name message"'.encode(DEFAULT_ENCODING)
            )
            client_socket.send(
                '\n3) To view the list of users, send "user"'.encode(DEFAULT_ENCODING)
            )

        self.selector.register(
            fileobj=client_socket,
            events=selectors.EVENT_READ,
            data=self.handle
            )

    @LogInfo('full')
    def handle(self, client_socket):
        try:
            message = client_socket.recv(MAX_SIZE_RECEIVE_DATA).decode(DEFAULT_ENCODING)
            message = self.clients[client_socket] + ': ' + message
            self.broadcast(message, client_socket)
        except Exception:
            self.broadcast(
                f'{self.clients[client_socket]} left!',
                client_socket
                )
            del self.clients[client_socket]
            self.selector.unregister(client_socket)
            client_socket.close()

    @LogInfo('full')
    def broadcast(self, message, client_socket):
        message_list = message.split()

        if message_list[1] in self.clients.values():
            for client, name in self.clients.items():
                if name == message_list[1]:
                    message_list.remove(message_list[1])
                    message_list.insert(0, '(private)')
                    message = ' '.join(message_list)
                    client.send(message.encode(DEFAULT_ENCODING))
        elif message_list[-1] == 'user':
            user_list = '\n'.join([_ for _ in self.clients.values()])
            client_socket.send(user_list.encode(DEFAULT_ENCODING))
        else:
            for client in self.clients:
                client.send(message.encode(DEFAULT_ENCODING))

    @LogInfo('full')
    def event_loop(self):
        while True:
            events = self.selector.select()

            for key, _ in events:
                callback = key.data
                callback(key.fileobj)


if __name__ == '__main__':
    addr, port = get_args()
    server = Server(addr, port)
    server.event_loop()
