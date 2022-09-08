import re

import pytest


def repl_5_by_cinq(str):
    return re.sub('5', 'cinq', str)

def repl_first_5by_cinq(str):
    return re.sub('5', 'cinq',str, 1)

def repl_note_by_x_not_sensitve(str):
    #pattern = r"note"
    # pattern = r"\d"
    pattern = r"(\b[1-9]{1}\b|\b(1[1-9])\b)"
    return re.sub(pattern, 'X',str, flags=re.IGNORECASE)


@pytest.fixture(scope='session')
def get_data():
    return "une chaine de test avec un chiffre 5 et un autre 5, un 3eme 5 et d'autre chiffre 3, 34, 6, 19"

def test_rep_5_by_cinq_should_return_str(get_data):
    result = repl_5_by_cinq(get_data)
    assert isinstance(result, str)

def test_rep_5_by_cinq_should_return_str_without_5(get_data):
    result = repl_5_by_cinq(get_data)
    assert "5" not in result

#### Test d'Armel ######
def test_replace_first_5occurence_return_a_string(get_data):
    result = repl_first_5by_cinq(get_data)
    assert isinstance(result, str)

def test_replace_first_5occurence_return_only_first_5(get_data):
    result = repl_first_5by_cinq(get_data)
    assert get_data.count("5") == result.count("5") + 1

def test_replace_all_notes_by_x_return_string(get_data):
    result = repl_note_by_x_not_sensitve(get_data)
    assert isinstance(result, str)

def test_replace_all_notes_by_x_return_no_note(get_data):
    result = repl_note_by_x_not_sensitve(get_data)
    # pattern = r"note"
    # pattern = r"\d"
    pattern = r"(\b[1-9]{1}\b|\b(1[1-9])\b)"
    assert not bool(re.search(pattern, result, flags=re.IGNORECASE))


