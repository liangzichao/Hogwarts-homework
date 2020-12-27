from Huogewozizuoye.test_appium.page.base_page import BasePage
from Huogewozizuoye.test_appium.page.main_page import MainPage
from Huogewozizuoye.test_appium.page.app import App

class Test_add_member():

    def test_add_contact(self):
        app = App()
        app.start()

        result = app.goto_main().goto_address().click_addmember().add_member_menual().add_contact()

        return result
