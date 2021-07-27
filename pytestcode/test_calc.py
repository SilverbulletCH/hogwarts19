
from pytestcode.calc import Calc
import pytest
import decimal


class TestCalc:

    def setup(self):
        self.calc = Calc()
        print('开始计算')

    def teardown(self):
        print('结束计算')

    @pytest.mark.parametrize("a, b, expect", [[1, 2, 3], [-1, -1, -2]])
    def test_add(self, a, b, expect):
        # calc = Calc()
        assert expect == self.calc.add(a, b)


    @pytest.mark.parametrize("a, b, expect", [[1,2,3],[2,3,5]])
    def test_add2(self,a, b, expect):
        self.calc.add(a, b)
        # assert expect == round(self.calc.add(a, b), 2)
        assert round(self.calc.add(a,b), 2) == expect