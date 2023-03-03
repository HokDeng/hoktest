
from selenium import webdriver

from base import base_driver
from page import text_page
from page.goodstype import shop_page,search_page,revise_page
from page.login import login_page, logout_page


# class Test_01(unittest.TestCase):
class Test_01:
    # 要填入的参数
    url = 'http://127.0.0.1/Login/login/index'#url
    username = ""
    password = ''
    typename='1000'#demo
    revisename=typename+"1"#demo
    driver = webdriver.Chrome()
    @classmethod
    def setup_class(self):
        print('----测试开始----')
        base_driver.BaseClass(self.driver, self.url).open()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    @classmethod
    def teardown_class(self):
        print('----测试结束----')
        logout_page.Logout_page(self.driver, self.url).logout()
        self.driver.quit()
    def setup(self):
        print("____用例开始____")
    def teardown(self):
        print("____用例结束____")
    def test_01(self):
        #登录
        loginin= login_page.Login_page(self.driver, self.url)
        loginin.input_username(self.username)
        loginin.input_password(self.password)
        loginin.click_login()
        text= text_page.Base_text(self.driver, self.url).loginText()
        assert text=="超级管理员"


#科发bos便利店管理
