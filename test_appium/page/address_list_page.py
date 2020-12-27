
from appium.webdriver.common.mobileby import MobileBy
from Huogewozizuoye.test_appium.page.member_invite_menu_page import MemberInviteMenuPage

from Huogewozizuoye.test_appium.page.base_page import BasePage

#通讯录页面

class AddressListPage(BasePage):




    def click_addmember(self):

        """
        添加成员
        :return:
        """
        #todo 点击添加成员
        #self.driver.swip_find("添加成员").click()
        self.swip_find_click(MobileBy.XPATH, "//*[@text='添加成员']")

        return MemberInviteMenuPage(self.driver)
