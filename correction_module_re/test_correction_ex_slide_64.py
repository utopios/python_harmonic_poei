import re


def test_question_1():
    str_with = "0xB0testcoucou"
    str_without = "testsans"
    assert bool(re.search(r'0xB0',str_with)) == True
    assert bool(re.search(r'0xB0',str_without)) == False

def question2(str_list):
    result = []
    result = list(filter(lambda element: bool(re.search(r'e', element)) == False, str_list))
    return result

def test_question_2():
   str_list = ["eee", "tttt", "ddd", "treee"]
   assert question2(str_list) == ["tttt", "ddd"]

