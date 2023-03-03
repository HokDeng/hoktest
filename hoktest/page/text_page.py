from base import base_driver
class Base_text(base_driver.BaseClass):
    login_ele=''#text的定位

    def loginText(self):
        #提取text
        text=self.gettext(self.login_ele)
        return text
