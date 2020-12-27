from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from selenium.webdriver.remote.mobile import Mobile

import pytest

class  Test_xueqiu(object):

    def setup_class(self):

        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        # android版本号
        desired_caps['platformVersion'] = '10'
        # 设备编号
        desired_caps['deviceName'] = 'WOC6QKFYPFR8YTIV'
        # app信息
        # 包名
        desired_caps['appPackage'] = 'com.xueqiu.android'
        #desired_caps['appPackage'] = 'com.tencent.wework'
        # 文件入口
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        #desired_caps['appActivity'] = '.launch.LaunchSplashActivity '
        # 中文的键盘
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = "True"
        desired_caps["settings[waitForIdleTimeout]"]: 0
        desired_caps["dontStopAppOnReset"] = "True"

        # desired_caps['autoGrantPermissions'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)


    def teardown_class(self):

        self.driver.quit()

    def test_search(self):

        #定位输入的搜索框
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
        #判断搜索框是否可用
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        #打印这个搜索框这个元素的左上角坐标和他的宽高
        self.driver.back()
        #向搜索框输入：alibaba
        self.driver.back()
        #判断阿里巴巴是否可见

        #如果可见，打印“搜索成功“” 点击，如果不可见，打印搜索失败

    def test_attr(self):
        # 定位输入的搜索框
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search")
        # 判断搜索框是否可用
        element = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search")

        search_enable = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enable == True:

            element.click()
            self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            alibabba = self.driver.find_element(MobileBy.XPATH,"//*[@id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            print(alibabba.get_attribute("displayed"))
            element_attribute = alibabba.get_attribute("displayed")
            if element_attribute == "true":
                print("搜索成功")
            else:
                print("搜索失败")


if __name__ == '__main__':
    pytest.main()


