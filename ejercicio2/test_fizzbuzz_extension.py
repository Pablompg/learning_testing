import pytest

from fizzbuzz_extenstion import fizzbuzz_extension


def test_fizzbuzz():
    assert fizzbuzz_extension(1) == "1"
    assert fizzbuzz_extension(3) == "Fizz"
    assert fizzbuzz_extension(5) == "Buzz"
    assert fizzbuzz_extension(15) == "FizzBuzz"
    assert fizzbuzz_extension(210) == "BuzzFizz"


@pytest.mark.parametrize("multiple_of_three", [3, 6, 9, 12])
def test_return_fizz_for_multiples_of_three(multiple_of_three: int):
    assert fizzbuzz_extension(multiple_of_three) == "Fizz"


@pytest.mark.parametrize("multiple_of_five", [5, 10, 20, 25])
def test_return_buzz_for_multiples_of_five(multiple_of_five: int):
    assert fizzbuzz_extension(multiple_of_five) == "Buzz"


@pytest.mark.parametrize("multiple_of_three_and_five", [15, 30, 45, 105])
def test_return_buzz_for_multiples_of_three_and_five(multiple_of_three_and_five: int):
    assert fizzbuzz_extension(multiple_of_three_and_five) == "FizzBuzz"


@pytest.mark.parametrize("multiple_of_three_and_five", [210, 420])
def test_return_buzz_for_multiples_of_three_five_and_seven_and_even(multiple_of_three_and_five: int):
    assert fizzbuzz_extension(multiple_of_three_and_five) == "BuzzFizz"
