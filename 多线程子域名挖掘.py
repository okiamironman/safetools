
import socket,sys,threading,queue

# 通过域名解析IP。域名存在则返回IP，不存在则报错，挖掘深度为1级
# 第1个参数为域名，不用带www，第2个参数为自定义线程数
# 使用时请把子域名挖掘字典放在同一路径下，可选自定义字典
def domain_dig(domain):
    while not q.empty():
        d2=q.get()
        ds=(d2+'.'+domain).replace('\n','')
        try:
            ip=socket.gethostbyname(ds)
            print(ds+'>>>'+ip)
        except Exception as e:
            pass

if __name__ == '__main__':
    domain=sys.argv[1]
    th_nums=sys.argv[2]
    q=queue.Queue()
    for d in open('子域名挖掘字典.txt'):
        q.put(d)
    for th_num in range(int(th_nums)):
        t=threading.Thread(target=domain_dig,args=(domain,))
        t.start()















# import socket,sys
#
# # 通过域名解析IP。域名存在则返回IP，不存在则报错，挖掘深度为1级
# def domain_dig(domain):
#     for d in open('子域名挖掘字典.txt'):
#         ds=(d+'.'+domain).replace('\n','')
#         try:
#             ip=socket.gethostbyname(ds)
#             print(ds+'>>>'+ip)
#         except Exception as e:
#             pass
#
# if __name__ == '__main__':
#     #输入域名不用带www
#     domain=sys.argv[1]
#     domain_dig(domain)
