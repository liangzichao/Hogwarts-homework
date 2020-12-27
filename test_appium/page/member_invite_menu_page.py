from Huogewozizuoye.test_appium.page.base_page import BasePage
from Huogewozizuoye.test_appium.page.contact_add_page import ContactAdd
from appium.webdriver.common.mobileby import MobileBy


class MemberInviteMenuPage(BasePage):

    pass

    def add_member_menual(self):


        """
        手动添加成员信息
        :return:
        """
        #todo 点击手动添加成员信息
        self.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加']")

        return ContactAdd(self.driver)