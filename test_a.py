# content of test_sample.py
import pytest


def func(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (3,4),
    (4,5),
    (5,6)
])
def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

def test_answer2():
    assert func(5) == 5

@pytest.fixture()#加了装饰器以后，就可以在想要调用它的地方直接使用
def login():
    print('登录操作')
    username = 'Tom'
    return username

class TestDemo:
    def test_a(self,login):#测试用例test_a需要登录，可以直接调用加了装饰器的login（）方法
        print(f"a,username = {login}")

    def test_b(self):
        print("b")

    def test_c(self,login):#测试用例test_c需要登录，可以直接调用加了装饰器的login（）方法
        print(f"c,username = {login}")

#用python解释器运行pytest文件
if __name__ == '__main__':
    pytest.main(['test_a.py::TestDemo','-v'])