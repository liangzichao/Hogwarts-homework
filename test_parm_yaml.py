
import pytest
import yaml

from Huogewozizuoye.calcuilator import Calculator


def get_datas():
    with open("./data.yaml", "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        # print(datas)

        data_add = datas["add"]
        data_subtract = datas["subtract"]
        data_ride = datas["ride"]
        data_divide = datas["divide"]
        add_ids = datas["myid"]
        # datas = datas["add"]

        # return [datas]

        return [data_add, add_ids, data_subtract, data_ride, data_divide]


class TestCalc:
    def setup_class(self):

        self.cal = Calculator()
        print("只执行一次计算开始")

    def teardown_class(self):
        print("只执行一次计算结束")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=get_datas()[1])
    def test_add(self,a,b,expect):

        assert expect == self.cal.add(a,b)


    @pytest.mark.parametrize("a,b,expect", get_datas()[2],ids=get_datas()[1])
    @pytest.mark.run(order=3)
    def test_sub(self, a, b, expect):

        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[3],ids=get_datas()[1])
    @pytest.mark.run(order=2)
    def test_mul(self, a, b, expect):


        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", get_datas()[4],ids=get_datas()[1])
    @pytest.mark.run(order=4)
    def test_dev(self, a, b, expect):

        assert expect == self.cal.dev(a, b)


def step1():
    print("打开浏览器")
def step2():
    print("注册新账号")
def step3():
    print("登录新账号")
# 解析测试步骤文件
def steps(path):
    with open(path) as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "step1" in step:
            step1()
        elif "step2" in step:
            step2()
        elif "step3" in step:
            step3()

def test_foo():
    steps("./steps.yaml")













