import yaml
from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By


class Test_Weixin_Demo(object):



    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("../web_selenium_weixin/data/data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")



    def teardown_class(self):

        #self.driver.quit()
        pass


    def test_Add_members(self):
        # 点击通讯录
        self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts").click()
        # .member_colLeft_top_addBtn

        # 点击添加部门按钮

        self.driver.find_element(By.XPATH, '//a[@class="member_colLeft_top_addBtnWrap js_create_dropdown"]').click()


        #点击输入框
        #click_add_input = By.CSS_SELECTOR,".qui_inputText ww_inputText"
        self.driver.find_element(By.XPATH,'//*[@id="js_contacts85"]/div/div[1]/ul/li[1]/a').click()

        self.driver.find_element(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys("lalal")

        # 点击下拉框

        self.driver.find_element( By.XPATH, '//a[@class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="1688853113247087_anchor"]/text()').click()
        # 输入点击保存
        #click_save = By.XPATH, "//a[@class='qui_btn ww_btn']"
        self.driver.find_element(By.XPATH,"//a[@class='qui_btn ww_btn ww_btn_Blue']").click()






# from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
# from selenium import webdriver
# import time
# import yaml
# # server 启动参数
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# class Test_Weixin_Demo(object):
#
#     def setup_class(self):
#         desired_caps = {}
#         # 设备信息
#         desired_caps['platformName'] = 'Android'
#         # android版本号
#         desired_caps['platformVersion'] = '10'
#         # 设备编号
#         desired_caps['deviceName'] = '127.0.0.1:7555'
#
#         # app信息
#         # 包名
#         # desired_caps['appPackage'] = 'com.xueqiu.android'
#         desired_caps['appPackage'] = 'com.tencent.wework'
#         # 文件入口
#         # desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
#
#         desired_caps['appActivity'] = '.launch.LaunchSplashActivity '
#         # 中文的键盘
#         desired_caps['unicodeKeyboard'] = True
#         desired_caps['resetKeyboard'] = True
#         desired_caps['noReset'] = "True"
#         desired_caps["settings[waitForIdleTimeout]"]: 0
#         # desired_caps['autoGrantPermissions'] = True
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
#     def teardown(self):
#
#         self.driver.quit()
#
#
#     def test_weixin(self):
#
#         #点击工作台的元素
#         self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()
#         #滚动查找元素
#         self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
#                                                       'scrollable(true).instance(0)).'
#                                                       'scrollIntoView(new UiSelector().'
#                                                       'text("打卡").instance(0));').click()
#
#         self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'出打卡')]").click()
#         #self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
#         self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
#         #显示等待
#         WebDriverWait(self.driver,10).until(lambda x: "外出打卡成功" in x.page_source)
#         print(self.driver.page_source)
#         assert "外出打卡成功" in self.driver.page_source
#





