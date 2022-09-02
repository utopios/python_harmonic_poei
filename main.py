
class Calculate:
    def __init__(self):
        pass
    def addition(self,a,b):
        return a+b

def test_given_addtion_when_addition_10_20_then_30():
    #Arrange
    cal = Calculate()
    #Act
    res = cal.addition(10,20)

    #Assert
    assert res == 30

if __name__ == '__main__':
    pass
