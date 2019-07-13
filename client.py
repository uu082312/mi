import socket
import threading
import time


def funA():
    print('---')
    # time.sleep(3)
    cli = socket.socket()
    cli.connect(('127.0.0.1', 8000))
    cli.send(b'haha')
    ret = cli.recv(1024)
    print(ret)
    cli.close()


if __name__ == '__main__':
    for i in range(10):
        th = threading.Thread(target=funA)
        th.start()