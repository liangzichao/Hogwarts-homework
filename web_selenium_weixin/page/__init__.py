from selenium.webdriver.common.by import By
"""以下为项目服务器地址"""
url1 = "https://work.weixin.qq.com/wework_admin/loginpage_wx?"
URL = "https://work.weixin.qq.com/wework_admin/frame#index"


"""以下为企业微信添加成员 配置信息"""
# 点击添加成员

click_add_Member = By.XPATH, "//span[@class='index_service_cnt_item_title']"

#输入用户名
add_username = By.ID,"username"
#输入别名
add_allias = By.ID,"memberAdd_english_name"
#输入唯一识别码
add_signboard = By.ID,"memberAdd_acctid"

#输入手机号
add_mobile = By.NAME,"mobile"
#输入座机
add_phone = By.ID, "memberAdd_telephone"
#输入邮箱
add_email = By.ID, "memberAdd_mail"
#输入地址
add_adress = By.ID, "memberEdit_address"
#输入职务
add_duty = By.ID, "memberAdd_title"
#输入点击保存
click_save = By.XPATH, "//a[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']"


"""以下为企业微信添加部门 配置信息"""
# 点击通讯录

click_add_attachment = By.XPATH, '//a[@id="menu_contacts"]/span[@class="frame_nav_item_title"]'


#点击添加按钮
click_add_button = By.CSS_SELECTOR,".member_colLeft_top_addBtn"
#.member_colLeft_top_addBtn

#点击添加部门按钮
add_signboard = By.XPATH,'//a[@class="js_create_party"]'

#点击下拉框
add_mobile = By.XPATH,'//a[@class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]'

#输入座机
add_phone = By.XPATH, '//a[@class="qui_btn ww_btn ww_btn_Blue"]'

#输入邮箱
add_email = By.ID, "memberAdd_mail"
#输入地址
add_adress = By.ID, "memberEdit_address"
#输入职务
add_duty = By.ID, "memberAdd_title"
#输入点击保存
click_save = By.XPATH, "//a[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']"



