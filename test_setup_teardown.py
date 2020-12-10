import pytest


def setup_module():
    print("setup:开始时整个文件只执行一次")


def teardown_module():
    print("teardown:结束时整个文件只执行一次")


def setup_function():
    print("setup: 不在类中的测试开始时都会执行")

def teardown_function():
    print("setup: 不在类中的测试结束时都会执行")

def test_tree():
    print("test-tree")

def test_four():

    print("test-four")

class TestClass(object):

    def setup_class(self):

        print("类里开始前只运行一次")

    def teardown_class(self):

        print("类里结束后只运行一次")

    def setup_method(self):

        print("每个用例开始前运行一次")

    def teardown_method(self):

        print("每个用例结束后后运行一次")

    def test_one(self):

        print("test-one")

    def test_two(self):

        print("test_two")


