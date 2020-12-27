from Huogewozizuoye.test_appium.page.main_page import MainPage

from appium import webdriver

from Huogewozizuoye.test_appium.page.base_page import BasePage


#封装的app driver驱动

class App(BasePage):

    def start(self):

        if self.driver is None:

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
        else:
            self.driver.launch_app()

    def goto_main(self):

        return MainPage(self.driver)