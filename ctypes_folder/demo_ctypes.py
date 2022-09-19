import ctypes

lib = ctypes.cdll.LoadLibrary("./c_librairies/linux/demo.so")
###pour windows
# lib = ctypes.windll.LoadLibrary("./c_librairies/windows/demo.dll")

print(lib.add_int(10,20))