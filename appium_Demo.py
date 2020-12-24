
#driver.quit()

#
# driver = webdriver.Chrome(executable_path="D:\Chrome\chromedriver.exe")
#
# driver.implicitly_wait(5)
#
# driver.maximize_window()
#
# # driver
# driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
#
# #driver.delete_all_cookies()
#
# print(driver.get_cookies())
#
# driver.quit()

# driver = webdriver.Chrome(executable_path="D:\Chrome\chromedriver.exe")
# driver.implicitly_wait(5)
# driver
# driver.get("https://www.baidu.com/")
#driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
# 设置debug地址
# opt = webdriver.ChromeOptions()
# opt.debugger_address = "127.0.0.1:9222"
# driver = webdriver.Chrome(options=opt)

# driver.delete_all_cookies()

# cookeies = driver.get_cookies()
# cookeies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
#              'value': '42343372452297115'},
#             {'domain': 'work.weixin.qq.com', 'expiry': 1608405833, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
#              'secure': False, 'value': '1dqljjd'},
#             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
#              'value': 'direct'},
#             {'domain': '.work.weixin.qq.com', 'expiry': 1639910297, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
#              'path': '/', 'secure': False, 'value': '0'},
#             {'domain': '.work.weixin.qq.com', 'expiry': 1610966298, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
#              'path': '/', 'secure': False, 'value': 'zh'}]
# for cookeie in cookeies:
#     driver.add_cookie(cookeie)
#
# driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
# # driver.find_element_by_id("menu_contacts").click()
# time.sleep(3)


#[{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '42343372452668175'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608406204, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '79sdsgr'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639910668, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610966670, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
# opt = webdriver.ChromeOptions()
#         # 设置debug地址
#         opt.debugger_address = "127.0.0.1:9222"
#         driver = webdriver.Chrome(options=opt)
#         driver.implicitly_wait(5)
#         driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#         driver.find_element_by_id("menu_contacts").click()
#         print(driver.get_cookies())
