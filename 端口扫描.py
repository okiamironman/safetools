
import socket,sys

def port_scan(ip,port):
    s = socket.socket()
    try:
        s.connect((ip,port))
        print(str(port)+':open')
    except Exception as e:
        print(str(port)+':close')
    finally:
        s.close()

if __name__ == '__main__':
    '''控制台交互模式'''
    ip=input('请输入要扫描的IP:')
    ports=input('请输入要扫描的端口号(如:80,135,443):')
    '''参数模式'''
    # 使用格式 ip ports
    # ip=sys.argv[1]
    # ports=sys.argv[2]
    # for port in ports.split(','):
    #     port_scan(ip,int(port))
