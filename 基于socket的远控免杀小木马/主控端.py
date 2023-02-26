import socket,sys

# 主控端-客户端-正向连接
# 连接服务端的IP和端口
# 输入命令发送执行
# 回显命令执行结果
# 输入q关闭连接,重新运行程序输入被控端的IP和端口即可继续连接(前提是输入q结束的连接)
import sys

ip,port=input('请输入被控端的ip和port，以空格分开: ').split()
port=int(port)
c=socket.socket()
c.connect((ip,port))
flag=''
while True:
    cmd_order=input('请输入要执行的命令: ')
    flag=cmd_order
    c.send(cmd_order.encode())
    if flag=='q':
        c.close()
        sys.exit()
    response = c.recv(102400).decode()
    print(response)
c.close()