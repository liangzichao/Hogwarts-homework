from Huogewozizuoye.web_selenium_weixin.base.base import Base


from Huogewozizuoye.web_selenium_weixin import page


from Huogewozizuoye.web_selenium_weixin.base.get_logger import GetLogger


class Page_Add_Member(Base):

    #点击添加成员
    def page_add_Member(self):

        self.base_click(page.click_add_Member)

    #输入用户名
    def page_add_username(self,username):

        self.base_input(page.add_username,username)

    #输入别名
    def page_add_allias(self,allias):
        self.base_input(page.add_allias,allias)

    #输入唯一识别码
    def page_add_signboard(self,sifnboard):
        self.base_input(page.add_signboard,sifnboard)

    #输入手机号
    def page_add_mobile(self,mobile):
        self.base_input(page.add_mobile,mobile)

    #输入座机
    def page_add_phone(self,phone):
        self.base_input(page.add_phone,phone)
    #输入邮箱
    def page_add_email(self, email):
        self.base_input(page.add_email, email)

    #输入地址
    def page_add_address(self, address):
        self.base_input(page.add_adress, address)

    #输入职务
    def page_add_duty(self,duty):
        self.base_input(page.add_duty,duty)

    #点击保存
    def page_save(self):
        self.base_click(page.click_save)

    #业务场景方法--->  组合业务方法 添加业务直接调用
    def page_save_Member(self,username,allias,sifnboard,mobile,phone,email,address,duty):
        #点击添加用户按钮
        #self.page_add_Member()
        #添加用户的身份 信息
        self.page_add_username(username)
        self.page_add_allias(allias)
        self.page_add_signboard(sifnboard)
        self.page_add_mobile(mobile)
        self.page_add_phone(phone)
        self.page_add_email(email)
        self.page_add_address(address)
        self.page_add_duty(duty)
        #添加动作
        self.page_save()

