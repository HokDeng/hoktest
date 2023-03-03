from selenium.webdriver.common.by import By
from base import base_driver
import time

from selenium import webdriver
class Logout_page(base_driver.BaseClass):
    user_ele=By.XPATH,"/html/body/div[1]/nav/div/div[2]/ul/li[2]/a"
    logout_ele=By.XPATH,"/html/body/div[1]/nav/div/div[2]/ul/li[2]/ul/li/a"
    user2_ele=By.XPATH,'/html/body/div[1]/nav/div/div[2]/ul/li[2]/a'
    logout2_ele=By.XPATH,'/html/body/div[1]/nav/div/div[2]/ul/li[2]/ul/li[4]/a'
    def logout(self):
        self.click(self.user_ele)
        time.sleep(0.5)
        self.click(self.logout_ele)
    def logout2(self):
        self.click(self.user2_ele)
        time.sleep(0.5)
        self.click(self.logout2_ele)