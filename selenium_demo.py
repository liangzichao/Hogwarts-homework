from selenium import webdriver

import time

class TestHogWARDS():

    def setup(self):
        self.driver = webdriver.Chrome(executable_path="D:\Chrome\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):

        self.driver.quit()

    def test_hogwards(self):

        self.driver.get("https://testerhome.com/")

        self.driver.find_element_by_link_text("社团").click()

        self.driver.find_element_by_link_text("求职面试圈").click()


        self.driver.find_element_by_css_selector('//div[@class="title media-heading"]/a').click()

