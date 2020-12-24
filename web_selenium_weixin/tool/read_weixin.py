
import yaml

from Huogewozizuoye.web_selenium_weixin.base.get_dirver import GetDriver
from Huogewozizuoye.web_selenium_weixin import data

# def get_datas():
#
#     with open("../data/weixin_data.yaml", "r", encoding="utf-8") as f:
#         datas = yaml.safe_load(f)
#
#     return datas
#
#         # return [data_add, add_ids, data_subtract, data_ride, data_divide]


if __name__ == '__main__':
    driver = GetDriver()

    driver.get_driver()