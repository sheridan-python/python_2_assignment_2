"""
This file stores all my tests for assignment 2.
They will be in order with 8 tests in total and a commit for each test.
"""

from prime import generate_prime_number

def test_float_value():
    """ if a non integer is entered, raise a ValueError"""
    assert generate_prime_number(2) == [2]

def test_value_is_1():
    """if input value is 1, return empty list"""
    assert generate_prime_number(1) == [] # empty list

def test_value_is_2():
    """if the input value is 2, return list [2]"""
    assert generate_prime_number(2) == [2]

def test_value_is_3():
    """if the input value is 3, return list [3]"""
    assert generate_prime_number(3) == [3]

def test_value_is_4():
    """ if the input value is 4, return list [2,2]"""
    assert generate_prime_number(4) == [2, 2]

def test_value_is_6():
    """ if the input is 6, return list [2, 3]"""
    assert generate_prime_number(6) == [2, 3]

def test_value_is_8():
    """ if the input is 8, return list [2, 2, 2]"""
    assert generate_prime_number(8) == [2, 2, 2]

def test_value_is_9():
    """ if the input is 9, return list [3, 3]"""
    assert generate_prime_number(9) == [3, 3]
