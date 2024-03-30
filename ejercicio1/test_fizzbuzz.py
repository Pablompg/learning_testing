import pytest

from fizzbuzz import fizzbuzz


def test_fizzbuzz():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"


@pytest.mark.parametrize("multiple_of_three", [3, 6, 9, 12])
def test_return_fizz_for_multiples_of_three(multiple_of_three: int):
    assert fizzbuzz(multiple_of_three) == "Fizz"


@pytest.mark.parametrize("multiple_of_five", [5, 10, 20, 25])
def test_return_buzz_for_multiples_of_five(multiple_of_five: int):
    assert fizzbuzz(multiple_of_five) == "Buzz"


@pytest.mark.parametrize("multiple_of_three_and_five", [15, 30, 45, 105, 210])
def test_return_buzz_for_multiples_of_three_and_five(multiple_of_three_and_five: int):
    assert fizzbuzz(multiple_of_three_and_five) == "FizzBuzz"


@pytest.mark.parametrize("regular_number", [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19])
def test_return_string_for_regular_numbers(regular_number: int):
    assert fizzbuzz(regular_number) == str(regular_number)
