import socket
sc = socket.socket()
sc.bind(('127.0.0.1', 12000))
sc.listen(1)
while(True):
    c, a = sc.accept()
    str = 'Connection successfully established'.encode()
    c.send(str)

    data = c.recv(1024)
    if data:
        print(data.decode())
        msg = raw_input("Enter your response\n")
        c.send(msg.encode())
    else:
        break

sc.close()
