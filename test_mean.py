from mean import *

def test_ints():
    input = [1, 2, 3, 4, 5]
    calculated_value = mean(input)
    expected_value = 3
    assert calculated_value == expected_value

def test_float():
    calculated_value = mean([1.0, 2.0, 3.0])
    expected_value = 2.0
    assert calculated_value == expected_value

def test_float_2():
    calculated_value = mean([1.0, 2.0, 3.0, 4.0, 5.0])
    expected_value = 3.0
    assert calculated_value == expected_value

def test_zeros():
    calculated_value = mean([0, 0, 0, 0, 0])
    expected_value = 0
    assert calculated_value == expected_value
