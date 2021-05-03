from math_series import __version__
from math_series.math_series import a ,fibonacci,locus


def test_version():
    assert __version__ == '0.1.0'

def test_one():
    assert a==6    

#---------"fibonacci"-----------------

def test_tow():
    expected=1
    actual=fibonacci(2)
    assert expected == actual

def test_three():
    expected=3
    actual=fibonacci(4)
    assert expected == actual

def test_four():
    expected=5
    actual=fibonacci(5)
    assert expected == actual

#locus test    
def test_five():
    expected=7
    actual=locus(4)
    assert expected == actual

def test_six():
    expected=2
    actual=locus(0)
    assert expected == actual

def test_seven():
    expected=11
    actual=locus(5)
    assert expected == actual