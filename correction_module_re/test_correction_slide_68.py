import re

import pytest


def repl_5_by_cinq(str):
    return re.sub('5', 'cinq', str)

@pytest.fixture(scope='session')
def get_data():
    return "une chaine de test avec un chiffre 5 et un autre 5, un 3eme 5 et d'autre chiffre 3, 34, 6"

def test_rep_5_by_cinq_should_return_str(get_data):
    result = repl_5_by_cinq(get_data)
    assert isinstance(result, str)

def test_rep_5_by_cinq_should_return_str_without_5(get_data):
    result = repl_5_by_cinq(get_data)
    assert "5" not in result