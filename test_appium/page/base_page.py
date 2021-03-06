from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver:WebDriver = None):

        self.driver = driver

    def find_element(self,by,locator,timeout=10, poll=1):

        return WebDriverWait(
            self.driver,timeout=timeout,poll_frequency=poll).\
            until(lambda x:x.find_element(by,locator))

    def find_elements(self, by, locator, timeout=10, poll=1):
        return WebDriverWait(
            self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_elements(by, locator))

    def find_and_click(self,by,locator):

        self.find_element(by,locator).click()

    def find_add_send(self,by,locator,text):

        self.find_element(by,locator).send_keys(text)

    def scroll_find(self,text):

        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def wait_for(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def swip_find(self, by, locator):
        self.driver.implicitly_wait(1)
        # 找到所有元素
        eles = self.driver.find_elements(by, locator)
        # 不停滑动，直到找到为止
        while len(eles) == 0:
            # 滑动
            self.driver.swipe(0, 600, 0, 400)
            eles = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    def swip_find_click(self, by, locator):
        self.swip_find(by, locator).click()





