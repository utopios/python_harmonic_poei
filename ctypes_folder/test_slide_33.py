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


@pytest.mark.parametrize("liste_cart_products, expected", [
    ([CartProduct(1, 200),CartProduct(2, 300)], 800),
    ([CartProduct(1, 200), CartProduct(-2, 300)], 0),
    ([CartProduct(1, -200), CartProduct(2, 300)], 0),
])
def test_calcule_total_correct_args_should_return_float(liste_cart_products, expected, get_lib):
    #Arrange
    # cart_products_list = [CartProduct(1,100), CartProduct(3,200)]
    cart_products_array = (CartProduct * len(liste_cart_products))(*liste_cart_products)

    #Act
    result = get_lib.calcule_total(cart_products_array, len(liste_cart_products))

    assert result == expected
    assert isinstance(result, float)