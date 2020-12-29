import pytest


class Test_Demo():
    # @pytest.mark.demo
    # def test_demo(self):
    #     a = 5
    #     b = -1
    #     assert a != b
    #     print("我的第一个测试用例")
    #
    # @pytest.mark.demo
    # @pytest.mark.smoke
    # #@pytest.mark.flaky(reruns=6,reuns_delay=1)
    # def test_two(self):
    #     a = 2
    #     b = 2
    #     #assert a != b
    #     # pytest.assume(a!=b)
    #     # pytest.assume(a>=b)
    #     # pytest.assume(a<=b)
    #
    #     print("我的第二个测试用例")
    #
    @pytest.mark.run(order=1)
    def test_one(self):

        assert 1==1

    def test_5(self):
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_two(self):
        assert 1 == 1

    def test_1(self):
        assert 1 == 1

    @pytest.mark.run(order=3)
    def test_2(self):
        assert 1 == 1

    def test_3(self):
        assert 1 == 1

    def test_4(self):
        assert 1 == 1

    def test_6(self):
        assert 1 == 1







