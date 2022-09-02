from calculate import Calculate


def inc(x):
    return x + 1

def test_answer_success():
    # """given inc when x is 4 then result is 5"""
    """inc(4) should be 5"""
    assert inc(4) == 5, "inc(4) should be 5"

def test_answer_fail():
    assert  inc(3) == 5

def test_calculate_addition():
    """calulate.addition(10,20) should be 30"""
    #Arrange
    calculate = Calculate()
    #Act
    result = calculate.addition(10,20)
    #Assert
    assert result == 30


