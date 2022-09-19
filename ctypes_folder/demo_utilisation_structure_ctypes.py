import ctypes

demo_struct = ctypes.cdll.LoadLibrary("./c_librairies/linux/exemple_struct.so")

demo_struct.area.argtypes= [ctypes.Structure]
demo_struct.area.restype = ctypes.c_float

class Rectange(ctypes.Structure):

    _fields_ = [
        ("width",ctypes.c_float),
        ("height", ctypes.c_float)
    ]
    def __init__(self, width, height):
        self.width = width
        self.height = height


result = demo_struct.area(Rectange(100.00, 300.00))

print(result)