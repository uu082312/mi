import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1', 8000))
sk.listen()

read_list = [sk] #存在socket对象或者conn对象
while True:
    rl, wl, xl = select.select(read_list, [], []) #在这等通知，轮训的去read_list查找有无连接响应
    for item in rl:
        if item == sk:
            conn, addr = sk.accept()
            read_list.append(conn)
        else:
            ret = item.recv(1024).decode('utf-8')
            print(ret)
            if not ret:
                item.close()
                read_list.remove(item)
            else:
                item.send(b'heihei')
