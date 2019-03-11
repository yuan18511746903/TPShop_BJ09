from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class LoginAndSignUpPage(BaseAction):

    phone_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title='登录注册 - 输入电话')
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    @allure.step(title='登录注册 - 输入密码')
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    @allure.step(title='登录注册 - 点击登录')
    def click_login(self):
        self.click(self.login_button)

    def is_login(self, content):
        """
        根据toast的部分内容，判断是否提示登录成功
        :param content:
        :return:
        """
        try:
            self.find_toast(content)
            return True
        except Exception:
            return False