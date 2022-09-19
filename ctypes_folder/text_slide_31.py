import ctypes

import pytest


@pytest.fixture(scope='session')
def get_lib():
    lib = ctypes.cdll.LoadLibrary("./c_librairies/linux/ex_3.so")
    ###pour windows
    #lib = ctypes.windll.LoadLibrary(".c_libraries/windows/ex_3.dll")
    lib.reverse.argtypes = [ctypes.Array, ctypes.c_int]
    return lib

def test_reverse_should_reverse_array(get_lib):
    ###Une liste en python
    liste = [1,2,3,4]

    ##Un tableau en pour une fonction en c
    tab = (ctypes.c_int * len(liste))(*liste)

    get_lib.reverse(tab, len(liste))
    result = [tab[i] for i in range(len(liste))]
    assert result == [4,3,2,1]

###Une version avec le mark parametrize

@pytest.mark.parametrize('liste, expected', [([1,2,3],[3,2,1]),([0,4,5,1],[1,5,4,0])])
def test_reverse_with_parametrize(liste, expected, get_lib):
    tab = (ctypes.c_int * len(liste))(*liste)
    get_lib.reverse(tab, len(liste))
    result = [tab[i] for i in range(len(liste))]
    assert result == expected