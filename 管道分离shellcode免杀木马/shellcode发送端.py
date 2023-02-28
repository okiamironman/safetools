import socket,base64

# shellcode发送端

ip,port=input('请输入被控端的ip和port: ').split()
port=int(port)
c=socket.socket()
c.connect((ip,port))

while True:
    cd=input('请输入要发送的shellcode: ')
    c.send(cd.encode())
c.close()

