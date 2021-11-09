import allure
import pytest
import time
import selenium


#测试报告里添加链接
@allure.testcase("http://www.github.com")
#添加测试报告的feature
@allure.feature("百度搜索")
#参数化，实现'allure','pytest','unittest'三个词的搜索
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = selenium.webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()
