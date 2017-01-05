from fib import *

def test_fib_0():
    fib0_expected = 1
    fib0_calculated = fib(0)
    assert fib0_expected == fib0_calculated

def test_fib_1():
    fib1_expected = 1
    fib1_calculated = fib(1)
    assert fib1_expected == fib1_calculated

def test_fib_3():
    fib3_expected = 3
    fib3_calculated = fib(3)
    assert fib3_expected == fib3_calculated
