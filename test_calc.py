
import pytest

from Huogewozizuoye.calcuilator import Calculator

class TestCalc:
    def setup_class(self):

        self.cal = Calculator()

    @pytest.mark.parametrize("a,b,expect",[(1,2,3),(-2,-3,-5),(100,200,300)]
                             ,ids=["num1","num2","num3"])
    def test_add(self,a,b,expect):

        assert expect == self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expect", [(3, 2, 1), (-3, 6, -9), (1000, 200, 800)]
        , ids=["num1", "num2", "num3"])
    def test_sub(self, a, b, expect):

        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [(1, 2, 2), (-2, -3, 6), (10, 200, 2000)]
        , ids=["num1", "num2", "num3"])

    def test_mul(self, a, b, expect):


        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [(100, 2, 50), (2, 10, 0.2), (1000, 200, 5)]
        , ids=["num1", "num2", "num3"])

    def test_dev(self, a, b, expect):

        assert expect == self.cal.dev(a, b)

