from fizz_buzz import fizz_buzz
import pytest

@pytest.mark.parametrize("number",[3,6,9])
def test_fizzbuzz_should_return_fizz_when_multiple_of_three(number):
    #Givern multiple of three
    #when execute fizz buzz
    result = fizz_buzz(number)
    #then result is Fizz
    assert result == "Fizz"


@pytest.mark.parametrize("number",[5,10,20])
def test_fizzbuzz_should_return_buzz_when_multiple_of_five(number):
    #Givern multiple of five
    #when execute fizz buzz
    result = fizz_buzz(number)
    #then result is Buzz
    assert result == "Buzz"


@pytest.mark.parametrize("number",[15,30,45])
def test_fizzbuzz_should_return_fizzbuzz_when_multiple_of_three_and_five(number):
    #Givern multiple of three and five
    #when execute fizz buzz
    result = fizz_buzz(number)
    #then result is FizzBuzz
    assert result == "FizzBuzz"


###Refactor of 3 first tests => by Hamdi
@pytest.mark.parametrize("number, result", [(3, 'Fizz'), (5, 'Buzz'), (15, 'FizzBuzz')])
def test_fizzbuzz_refactor(number, result):
    res = fizz_buzz(number)
    assert res == result


@pytest.mark.parametrize("number",[1,7,37])
def test_fizzbuzz_should_return_number_when_neither_multiple_of_three_and_five(number):
    #Givern multiple of three and five
    #when execute fizz buzz
    result = fizz_buzz(number)
    #then result is number
    assert result == str(number)

def test_fizzbuzz_should_raise_exception_when_not_int():
    with pytest.raises(TypeError):
        fizz_buzz("test")
