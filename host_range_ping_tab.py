import subprocess
from tabulate import tabulate


def main(host_start, host_stop):
    host = '.'.join(host_start.split('.')[:3]) 
    host_start = int(host_start.split('.')[-1])
    host_stop = int(host_stop.split('.')[-1])

    host_list = []

    for addr in range(host_start, host_stop):
        ping = subprocess.call(['ping', '-c', '1', f'{host}.{addr}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if ping:
            host_list.append(('-----------',f'{host}.{addr}'))
        else:
            host_list.append((f'{host}.{addr}','-------------'))

    print(tabulate(host_list, headers=['reachable', 'unreachable']))


if __name__ == '__main__':
    main('127.0.0.0', '127.0.0.5')