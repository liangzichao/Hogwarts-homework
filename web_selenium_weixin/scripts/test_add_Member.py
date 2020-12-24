import pytest
import yaml

from Huogewozizuoye.web_selenium_weixin.page.page_add_Member import Page_Add_Member

from Huogewozizuoye.web_selenium_weixin.base.get_logger import GetLogger

from Huogewozizuoye.web_selenium_weixin.base.get_dirver import GetDriver

from Huogewozizuoye.web_selenium_weixin import page

from Huogewozizuoye.web_selenium_weixin import data
# 获取log日志器
log = GetLogger().get_logger()

def get_datas():

    with open("../data/weixin_data.yaml", "r", encoding="utf-8") as f:
        datas = yaml.safe_load(f)

    return datas

#新加 添加成员 测试类  并用pytest框架实现
class Test_add_Member(object):

    def setup_class(self):
        try:
            #实例化并获取driver
            self.driver = GetDriver().get_driver()
            #self.driver.get(page.url1)

            # with open("data.yaml", encoding="UTF-8") as f:
            #     yaml_data = yaml.safe_load(f)
            #     for cookie in yaml_data:
            #         self.driver.add_cookie(cookie)
            #
            # self.driver.get(page.URL)

            # 实例化 Page_Add_Member()
            self.add_membe = Page_Add_Member(self.driver)
            # 点击添加人员连接
            self.add_membe.page_add_Member()
        except Exception as e:
                log.error("错误：{}".format(e))
                # 截图
                self.add_membe.base_get_image()

    def teardown_class(self):

        # 关闭drier驱动对象
        GetDriver().quit_driver()

    @pytest.mark.parametrize("username,allias,sifnboard,mobile,phone,email,address,duty",get_datas())
    def test_add_member(self,username,allias,sifnboard,mobile,phone,email,address,duty):
        try:
            # 调用 登录业务方法
            self.add_membe.page_save_Member(username,allias,sifnboard,mobile,phone,email,address,duty)

        except Exception as e:

            log.error("错误：{}".format(e))
            # 截图
            self.add_membe.base_get_image()














