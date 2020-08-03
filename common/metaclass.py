import inspect
import re

from .decorators import LogInfo


class ClientVerifier(type):
    @LogInfo('full')
    def __init__(self, clsname, bases, attrs):
        pattern_call = '(\.accept|\.listen){1}'
        x = inspect.getsourcelines(self)[0]
        for i in x:
            if re.search(pattern_call, i.strip()):
                print('Invalid call "accept" or "listen"!')
                raise TypeError('Invalid call "accept" or "listen"!')


class ServerVerifier(type):
    @LogInfo('full')
    def __init__(self, clsname, bases, attrs):
        pattern_call = '(\.connect){1}'
        x = inspect.getsourcelines(self)[0]
        for i in x:
            if re.search(pattern_call, i.strip()):
                print('Invalid call "connect"!')
                raise TypeError('Invalid call "accept" or "listen"!')
