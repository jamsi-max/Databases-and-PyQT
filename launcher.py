import subprocess
from platform import system
import sys


def main(count=2):
    if system() == 'Linux':
        subprocess.call(['gnome-terminal', '-e', 'python server.py'])
        for _ in range(count):
            subprocess.call(['gnome-terminal', '-e', 'python client.py'])
    elif system() == 'Windows':
        subprocess.call('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        for _ in range(count):
            subprocess.call('python client.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        

if __name__ == '__main__':
    if sys.argv[1].isdigit() and int(sys.argv[1])<10:
        main(int(sys.argv[1]))
    else:
        main()