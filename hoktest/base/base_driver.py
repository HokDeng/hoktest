
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from selenium.webdriver.support.ui import Select
class BaseClass(object):
    def __init__(self,driver,url):
        self.driver=driver
        self.url=url
    def find_element(self,ele):
        x,y=ele
        element=WebDriverWait(self.driver,20).until(lambda a:a.find_element(x,y))
        return element

    def send_keys(self,ele,value):
        self.find_element(ele).send_keys(value)#ele是页面定位，value是输入内容
    def click(self,*ele):
        self.find_element(*ele).click()
    def open(self):
        self.driver.get(self.url)
    def gettext(self,ele):
        text=self.driver.find_element_by_xpath(ele).get_attribute('textContent')
        return text
    def getvalue(self,ele):
        value=self.driver.find_element_by_xpath(ele).get_attribute('value')
        return value
    def clear(self,*ele):
        self.find_element(*ele).clear()
    def select(self,ele,text):
        Select(self.driver.find_element_by_xpath(ele)).select_by_visible_text(text)
    def refresh(self):
        self.driver.refresh()
    def getnowdata(self):
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        return today
    def getyesterday(self):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        return str(yesterday)
    def getsevendata(self):
        today = datetime.date.today()
        sevenday = datetime.timedelta(days=7)
        day = today - sevenday
        return str(day)