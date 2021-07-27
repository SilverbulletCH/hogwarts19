import pytest
import yaml

from pytestcode.calc import Calc

def get_data():
    with open(r"C:\Users\89703\PycharmProjects\hogwarts19\pytestcode\datas\calc1.yaml") as f:
        datas = yaml.safe_load(f)
        return datas

# def test_datas():
#     print(get_data()['add_data'])

class TestCalc:


     def setup(self):
         self.calc = Calc()
         print('开始计算')

     def teardown(self):
         print('结束计算')

     @pytest.mark.parametrize("a, b, expect", get_data()['add_data']['datas'], ids=get_data()['add_data']['ids'])
     def test_add(self, a, b, expect):
         self.calc.add(a, b)
         assert round(self.calc.add(a, b), 2) == expect