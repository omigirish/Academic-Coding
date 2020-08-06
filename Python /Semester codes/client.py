import socket
sc = socket.socket()
sc.connect(('127.0.0.1', 12000))
print(sc.recv(1024).decode())
msg = raw_input("Enter any message\n")
while(msg!= 'Exit'):
    sc.send(msg.encode())
    data = sc.recv(1024)
    print(data.decode())
    msg = raw_input("Enter any message\n")
sc.close()


