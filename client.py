import threading
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
    )

from common.variables import (
    DEFAULT_ENCODING,
    MAX_SIZE_RECEIVE_DATA
    )
from common.utils import (
    args_validation,
    get_args
    )

from common.decorators import LogInfo


class Client:
    client_socket = socket(AF_INET, SOCK_STREAM)
    event = threading.Event()
    nickname = ''

    @LogInfo('full')
    def __init__(self, addr, port):
        self.nickname = input('Input your nickname: ')

        self.client_socket.connect(args_validation(addr, port))

        send_message_thread = threading.Thread(
            target=self.send_message,
            daemon=True
            )
        receive_thread = threading.Thread(
            target=self.receive,
            daemon=True
            )

        receive_thread.start()
        send_message_thread.start()

        receive_thread.join()
        send_message_thread.join()

    @LogInfo('full')
    def receive(self):
        while True:
            try:
                message = self.client_socket.recv(
                    MAX_SIZE_RECEIVE_DATA
                    ).decode(DEFAULT_ENCODING)
                if message == 'GET_NICK':
                    self.client_socket.send(
                        self.nickname.encode(DEFAULT_ENCODING)
                        )
                else:
                    print(message)
                    self.event.set()
            except Exception:
                print('An error occured!')
                self.client_socket.close()
                break

    @LogInfo('full')
    def send_message(self):
        self.event.wait()
        while True:
            message = f'{input()}'
            self.client_socket.send(message.encode(DEFAULT_ENCODING))


if __name__ == '__main__':
    addr, port = get_args()
    client = Client(addr, port)
