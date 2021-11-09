import pytest
import yaml


class TestDemo:

    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的IP是：",env["test"])#通过key值获取对应的value
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的IP是：", env["dev"])  # 通过key值获取对应的value


    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))
