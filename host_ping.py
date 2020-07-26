import subprocess
import ipaddress
import re

def addr_valid(host):
    pattern_ip = '^([0-9]{1,3}[\.]){3}[0-9]{1,3}$'
    pattern_host = '^(?:[a-zA-Z0-9-_]+\.)+(ru|com)$'

    if re.fullmatch(pattern_ip, host):
        return ipaddress.ip_address(host)
    elif re.fullmatch(pattern_host, host):
        return host
    else:
        raise ValueError(f'{host} - invalid address')



def ping_host(host):
    return subprocess.call(['ping', '-c', '1', f'{host}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def host_ping(host_list):
    for host in host_list:
        host_valid =  addr_valid(host)
        
        ping = ping_host(host_valid)

        if ping:
            print(f'{host} -> NOT available')
        else:
            print(f'{host} -> available')


if __name__ == '__main__':
    host_ping(['yandex.ru', 'mail.ru', '127.0.0.1', '--.ru.'])