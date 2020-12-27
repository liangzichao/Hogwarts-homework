from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.webdriver import WebDriver

class Test_Weixin_Demo(object):

    def setup_class(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        # android版本号
        desired_caps['platformVersion'] = '10'
        # 设备编号
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # app信息
        # 包名
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appPackage'] = 'com.tencent.wework'
        # 文件入口
        # desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity '
        # 中文的键盘
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['noReset'] = "True"
        desired_caps["settings[waitForIdleTimeout]"]: 0
        # desired_caps['autoGrantPermissions'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(10)

    def trardown_class(self):
        self.driver.quit()

    def test_add_address_book(self):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']").click()
        # 向下滑动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               'text("添加成员").instance(0));').click()

        # 手动添加
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        #
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]').send_keys("梁子超")

        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"性别")]/..//*[@text="男"]').click()

        #self.driver.find_element(MobileBy.XPATH, "//*[[@text='男']]").click()

        def wait_ele_for(driver: webdriver):
            eles = driver.find_elements(MobileBy.XPATH,'//*[@text="女"]')

            return len(eles) > 0


        WebDriverWait(self.driver,10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()


        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"手机")]/..//*[@text="手机号"]').send_keys("15093943706")

        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/ie7" and @text="保存"]').click()











