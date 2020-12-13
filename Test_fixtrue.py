import pytest




# 执行结果：
# test_abc.py
# ------->setup_class
# ------>test_a  # 只执行了函数test_a
#
# ------->teardown_class
# s  # 跳过函数

# fixture修饰器来标记固定的工厂函数, 在其他函数，模块，类或整个工程调用它时会被激活并优先执行,
# 通常会被用于完成预置处理和重复操作。

"""
 方法：fixture(scope="function", params=None, autouse=False, ids=None, name=None)
    常用参数:
        scope：被标记方法的作用域
            function" (default)：作用于每个测试方法，每个test都运行一次
            "class"：作用于整个类，每个class的所有test只运行一次
            "module"：作用于整个模块，每个module的所有test只运行一次
            "session：作用于整个session(慎用)，每个session只运行一次
        params：(list类型)提供参数数据，供调用标记方法的函数使用
        autouse：是否自动运行,默认为False不运行，设置为True自动运行

"""
"""
yaml的语法：

1、在yaml里面，结构通过缩进来表示，
连续的项目（如：数组元素、集合元素）通过减号“-”来表示，
map结构里面的键值对（key/value）用冒号“:”来分割。
yaml也有用来描述好几行相同结构数据的缩写语法，
数组用“[]”包括起来，hash用“{}”来包括。这几乎就是yaml的全部语法了。


"""
"""
使用yaml的注意事项

1、在yaml里面，结构通过缩进来表示，yaml不支持制表符tab缩进，请使用空格缩进；
2、如果参数是以空格开始或结束的字符串，应使用单引号把他包进来。如果一个字符串参数包含特殊字符，也要用单引号包起来。下面是示例：
如果要保存类似    http://www.bai'u.com这样的数据时，下面这种写法是错误的：

website:{  baidu: http://www.bai'u.com }#写法错误，因为没有用单引号括起来；

website:{  baidu: 'ttp://www.bai''u.com'}#写法正确，如果字符串中本身包含单引号，则需要用‘’进行转义；如果字符串开头或结尾包含空格，则需要用单引号将整个字符串包裹

在书写键值对时，如果键名或键值包含非英文字母和数字，应该用引号括起来，例如： '标题': '这是我的第一本杂志'
3、每个冒号后面一定要有一个空格（以冒号结尾不需要空格，表示文件路径的模版可以不需要空格），这里指的是键值对，例如：

mykey: my_value

4、 想要表示列表项，使用一个短横杠加一个空格。多个项使用同样的缩进级别作为同一个列表的一部分

"""

# class Test_ABC:
#     def setup_class(self):
#         print("------->setup_class")
#
#     def teardown_class(self):
#         print("------->teardown_class")
#
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#
#     @pytest.mark.skipif(condition=2 > 1, reason="跳过该函数")  # 跳过测试函数test_b
#     def test_b(self):
#         print("------->test_b")
#         assert 0
#


class Test_firstFile():

    def test_one(self,myfixture):
        print("执行test_one")
        assert 2+3==5

    def test_two(self):
        print("执行test_two")
        assert 1==1

    def test_three(self):
        print("执行test_three")
        assert 1 + 1 == 2



import yaml
def add_function(a,b):
    return a+b

@pytest.mark.parametrize("a,b,expected",
                         yaml.safe_load(open("./data1.yaml"))["datas"],
                         ids=yaml.safe_load(open("./data1.yaml"))["myid"])

def test_add(a,b,expected):
    assert add_function(a,b) == expected