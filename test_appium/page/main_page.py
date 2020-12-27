
from Huogewozizuoye.test_appium.page.address_list_page import AddressListPage
from Huogewozizuoye.test_appium.page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class MainPage(BasePage):
    """
    首页po

    """

    address_element = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']")

    def goto_message(self):
        """
            进入到消息页
        :return:
        """
        pass


    def goto_address(self):

        """
        进入通讯录
        :return:
        """
        #todo点击通讯录

        self.find_and_click(*self.address_element)

        return AddressListPage(self.driver)