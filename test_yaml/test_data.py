import pytest
import yaml


class TestData:
    # 使用字符串参数化
    #@pytest.mark.parametrize("a,b",[(10,20),(11,20),(12,20)])
    # 使用列表list参数化
    #@pytest.mark.parametrize(["a","b"], [(10, 20), (11, 20), (12, 20)])
    # 使用元祖tuple参数化
    #@pytest.mark.parametrize(("a","b"), [(10, 20), (11, 20), (12, 20)])

    #使用yaml
    @pytest.mark.parametrize(("a", "b"),yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        #a = 10
        #b = 20
        print(a+b)


    '''
    def test_data2(self):
        a = 11
        b = 20
        print(a+b)

    def test_data3(self):
        a = 12
        b = 20
        print(a+b)
    '''