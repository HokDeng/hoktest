from selenium.webdriver.common.by import By
from base import base_driver
class Login_page(base_driver.BaseClass):
    #写页面元素
    username_ele=By.XPATH,'//*[@id="username"]'
    password_ele=By.XPATH,'//*[@id="password"]'
    login_ele=By.XPATH,'/html/body/div/div/div/div[2]/div/div/form/div/div[2]/button'

    def input_username(self,username):
        self.send_keys(self.username_ele,username)#self.username_ele是页面定位，username是输入内容
    def input_password(self,password):
        self.send_keys(self.password_ele,password)
    def click_login(self):
        self.click(self.login_ele)