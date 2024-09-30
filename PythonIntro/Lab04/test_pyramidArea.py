# Author: Hogan Lin
# Date: Sept 30th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: create the five different test case for unit test
import pytest
from pyramidArea import calcBaseArea, calcSideArea, prntSurfArea

# Test for calcBaseArea by passing 15 and asserting the result is 225
def testCalcBaseArea15():
    assert calcBaseArea(15) == 225

# Test for calcBaseArea by passing "5", expecting a failure since the input should be a float
@pytest.mark.xfail(reason="Input should not be a string")
def testCalcBaseAreaString():
    calcBaseArea("5")  

# Test calcSideAreaBetween with side=15, height=5 check the result is between 270.41 and 270.42
def testCalcSideAreaBetween15And5():
    result = calcSideArea(15, 5)
    assert 270.41 < result < 270.42

# Test calcSideAreaBetween with side=10, height=3 check the result is 116.62 when rounded to two decimal
def testCalcSideArea10And3():
    result = calcSideArea(10, 3)
    assert round(result, 2) == 116.62

# Test prntSurfArea by passing in side=15, height=10 and use mark to skip it
@pytest.mark.skip(reason="This function only prints text to the screen")
def testPrntSurfArea15And10():
    prntSurfArea(15, 10)  # This is just to skip the function test as requested
