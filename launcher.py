import subprocess
from platform import system


def main():
    if system() == 'Linux':
        subprocess.call(['gnome-terminal', '-e', 'python server.py'])
        subprocess.call(['gnome-terminal', '-e', 'python client.py'])
        subprocess.call(['gnome-terminal', '-e', 'python client.py'])
    elif system() == 'Windows':
        subprocess.call('python python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('python python client.py', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('python python client.py', creationflags=subprocess.CREATE_NEW_CONSOLE)


if __name__ == '__main__':
    main()