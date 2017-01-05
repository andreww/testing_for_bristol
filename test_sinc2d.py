from sinc2d import sinc2d
import numpy as np

def test_y():
    x=1
    expec = np.sin(x) / x
    calc = sinc2d(x,0)
    assert calc == expec

def test_x():
    y=1
    expec = np.sin(y) / y
    calc = sinc2d(0,y)
    assert calc == expec

def test_sinc2d_corner():
    x, y = 0, 0
    expect = 1
    calc = sinc2d(x,y)
    assert calc == expect
