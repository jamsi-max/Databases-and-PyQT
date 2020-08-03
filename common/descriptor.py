import sys
from .decorators import LogInfo

class PortVerifier:
    def __set_name__(self, owner, name):
        self.__name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.__name)

    @LogInfo('full')
    def __set__(self, instans, value):
        if value < 1024 or value > 65535:
            print('The port must be in the range from 1025 to 65534!')
            raise KeyError('The port must be in the range from 1025 to 65534!')
            sys.exit(1)
        else:
            instans.__dict__[self.__name] = value


class AddrVerifier:
    def __set_name__(self, owner, name):
        self.__name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.__name)

    @LogInfo('full')
    def __set__(self, instans, value):
        if len(value.split('.')) != 4 and value != 'localhost':
            raise KeyError('The address must be 0.0.0.0 or localhost!')
            sys.exit(1)
        else:
            instans.__dict__[self.__name] = value
