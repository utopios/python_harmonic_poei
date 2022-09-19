import ctypes

lib = ctypes.cdll.LoadLibrary("./c_librairies/linux/demo.so")
###pour windows
# lib = ctypes.windll.LoadLibrary("./c_librairies/windows/demo.dll")

#print(lib.add_int(10,20)) => #utilisation de add_int de la librairies
# var1 = ctypes.c_float(10.0)
# var2 = ctypes.c_float(20.0)
# lib.add_float.argtypes = [ctypes.c_float, ctypes.c_float]
# lib.add_float.restype = ctypes.c_float
# result = lib.add_float(var1,var2)
# print(result) #=> utilisation de add_float de librairies



a = ctypes.c_float(10)
b = ctypes.c_float(20)
c = ctypes.c_float()

##Utilisation de byref

#lib.add_float_ref(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))


##Utilisation de pointer
a_pointer= ctypes.pointer(a)
b_pointer = ctypes.pointer(b)
c_pointer = ctypes.pointer(c)

lib.add_float_ref(a_pointer,b_pointer, c_pointer)
print(c.value)