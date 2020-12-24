from selenium import webdriver

from Huogewozizuoye.web_selenium_weixin import page

import yaml
class GetDriver:
    driver = None

    # 获取 driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 获取driver
            cls.driver = webdriver.Chrome()
            # 最大化浏览器
            cls.driver.maximize_window()
            # 打开url
            cls.driver.get(page.url1)
            #
            with open("../data/data.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    cls.driver.add_cookie(cookie)

            cls.driver.get(page.URL)

        # 返回 driver
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空操作
            cls.driver = None

if __name__ == '__main__':
    GetDriver().get_driver()

##轴定位