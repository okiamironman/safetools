
import socket,sys,threading,queue

# 多线程全端口扫描，参数模式，可自定义线程数
# 第1个参数为要扫描的IP，第2个参数为自定义线程数

def full_port_scan(ip):
    while not q.empty():
        port=q.get()
        s=socket.socket()
        try:
            s.connect((ip,port))
            print(ip+':'+str(port)+':open')
        except Exception as e:
            print(ip+':'+str(port)+':close')
            # pass
        finally:
            s.close()
if __name__ == '__main__':
    ip=sys.argv[1]
    th_nums=sys.argv[2]

    q=queue.Queue()
    for port in range(1,65536):
        q.put(port)
    for th_num in range(int(th_nums)):
        t=threading.Thread(target=full_port_scan,args=(ip,))
        t.start()
