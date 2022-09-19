import ctypes

import pytest


@pytest.fixture(scope='session')
def get_lib():
    lib = ctypes.cdll.LoadLibrary("./c_librairies/linux/ex_2.so")
    ###pour windows
    #lib = ctypes.windll.LoadLibrary(".c_libraries/windows/ex_2.dll")
    lib.concat_two_string.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    lib.concat_two_string.restype = ctypes.c_char_p
    return lib

@pytest.mark.parametrize("str_1,str_2, expected", [(b"Hello ", b"World", "Hello World"), (b"abadi", b" ihab", "abadi ihab")])
def test_concat_two_string_result(str_1, str_2, expected, get_lib):
    # str_1 = ctypes.c_char_p(str_1)
    # str_2 = ctypes.c_char_p(str_2)
    result = get_lib.concat_two_string(ctypes.c_char_p(str_2), ctypes.c_char_p(str_1))
    assert result.decode("utf-8") == expected