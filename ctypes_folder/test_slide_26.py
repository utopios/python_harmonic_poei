import ctypes

import pytest


@pytest.fixture(scope='session')
def get_lib():
    lib = ctypes.cdll.LoadLibrary("./c_librairies/linux/cart.so")
    ###pour windows
    #lib = ctypes.windll.LoadLibrary(".c_libraries/windows/cart.dll")
    lib.is_correct_product.argtype = ctypes.c_int
    ##ou
    #lib.is_correct_product.argtypes = [ctypes.c_int]
    lib.is_correct_product.restype = ctypes.c_bool
    lib.total_item.argtypes = [ctypes.c_int, ctypes.c_float]
    lib.total_item.restype = ctypes.c_float
    return lib


def test_is_correct_product_when_id_12_should_be_true(get_lib):
    id = ctypes.c_int(12)
    assert get_lib.is_correct_product(id) == True


def test_is_correct_product_should_be_false(get_lib):
    id1 = ctypes.c_int(10)
    id2 = ctypes.c_int(-3)
    assert get_lib.is_correct_product(id1) == False
    assert get_lib.is_correct_product(id2) == False


@pytest.mark.parametrize("id_product, expected", [(10,False),(12,True), (-12,False), (13,False)])
def test_is_correct_product_all_cases(id_product, expected, get_lib):
    assert get_lib.is_correct_product(id_product) == expected


@pytest.mark.parametrize("qty, price, expected", [(3,100, 300), (-1,100, 0), (1,-100, 0)])
def test_total_item_all_cases(qty, price, expected, get_lib):
    assert get_lib.total_item(qty, price) == expected