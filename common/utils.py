import sys
import argparse

from common.decorators import LogInfo
from common.variables import (
    DEFAULT_ADDR,
    DEFAULT_PORT
    )


class PortError(Exception):
    pass


class AddrError(Exception):
    pass


@LogInfo('full')
def args_validation(addr, port):
    '''
    Validation of data entered by the user

    return tuple(addr: str, port: int)
    '''
    try:
        if port < 1024 or port > 65535:
            raise PortError
        if not addr:
            raise AttributeError
        if len(addr.split('.')) != 4 and addr != 'localhost':
            raise AddrError
        return (addr, port)
    except PortError:
        print('The port must be in the range from 1025 to 65534!')
        sys.exit(1)
    except ValueError:
        sys.exit(1)
    except AddrError:
        print('The address must be 0.0.0.0 or localhost!')
        sys.exit(1)
    except AttributeError:
        print('The address must be 0.0.0.0 or localhost!')
        sys.exit(1)


def get_args():
    parse = argparse.ArgumentParser()

    parse.add_argument('-a', type=str, default=DEFAULT_ADDR, help='Add addres')
    parse.add_argument('-p', type=int, default=DEFAULT_PORT, help='Add port')
    args = parse.parse_args()

    return (args.a, args.p)
