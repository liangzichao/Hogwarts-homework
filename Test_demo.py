import pytest


# def add_function(a,b):
#
#     return a+b


#class Test_demo(object):

@pytest.mark.parametrize("a",[0,1,5])
@pytest.mark.parametrize("b",[2,3,8])

def test_one(a,b):

    print("测试数据组合：a--->{},b--->{}".format(a,b))


def test_two():
    a = 1
    b = 2
    assert a != b
    print("这是我的第二个测试用例")









