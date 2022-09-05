import pytest


def div(x, y):
    ##On essaye une opération de div par zero
    try:
        x / y
    except ZeroDivisionError:
        ##Si exception, on lève l'expection
        raise ZeroDivisionError
    finally:
        ##Partie à executer dans tout les cas
        pass
    # if y == 0:
    #     raise ZeroDivisionError
    # return x / y


def test_div():
    ##context raises de pytest pour vérfier l'exception
    with pytest.raises(ZeroDivisionError):
        #Bloc de code qui leve l'exception
        div(10, 0)