import subprocess


def main(host_start, host_stop):
    host = '.'.join(host_start.split('.')[:3]) 
    host_start = int(host_start.split('.')[-1])
    host_stop = int(host_stop.split('.')[-1])

    for addr in range(host_start, host_stop):
        ping = subprocess.call(['ping', '-c', '1', f'{host}.{addr}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if not ping:
            print(f'{host}.{addr} -> available')
        else:
            print(f'{host}.{addr} -> not a valid host name')


if __name__ == '__main__':
    main('127.0.0.0', '127.0.0.156')