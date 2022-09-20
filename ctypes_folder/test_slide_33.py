import ctypes

import pytest


class CartProduct(ctypes.Structure):
    _fields_ = [
        ("qty", ctypes.c_int),
        ("price", ctypes.c_float)
    ]

    def __init__(self, qty, price):
        self.qty = qty
        self.price = price

@pytest.fixture(scope='session')
def get_lib():
    lib = ctypes.cdll.LoadLibrary('./c_librairies/linux/ex_4.so')
    lib.calcule_total.argtypes = [ctypes.Array,ctypes.c_int]
    lib.calcule_total.restype = ctypes.c_float
    return lib


def test_calcule_total_correct_args_should_return_float(get_lib):
    #Arrange
    cart_products_list = [CartProduct(1,100), CartProduct(3,200)]
    cart_products_array = (CartProduct * len(cart_products_list))(*cart_products_list)

    #Act
    result = get_lib.calcule_total(cart_products_array, len(cart_products_list))

    assert result == 700