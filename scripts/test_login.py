import random
import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # @pytest.mark.parametrize(("phone", "password", "expect"), analyze_file("login_data", "test_login"))
    # def test_login(self, phone, password, expect):
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_and_sign_up()
    #     self.page.login_and_sign_up_page.input_phone(phone)
    #     self.page.login_and_sign_up_page.input_password(password)
    #     self.page.login_and_sign_up_page.click_login()
    #     assert self.page.login_and_sign_up_page.is_login(expect)

    # @pytest.mark.parametrize(("phone", "password"), analyze_file("login_data", "test_login_miss_part"))
    # def test_login_miss_part(self, phone, password):
    #     # 首页点击 我的
    #     self.page.home.click_mine()
    #     # 我的点击 登录注册
    #     self.page.mine.click_login_and_sign_up()
    #     # 登录注册输入 手机号
    #     self.page.login_and_sign_up_page.input_phone(phone)
    #     # 登录注册输入 密码
    #     self.page.login_and_sign_up_page.input_password(password)
    #     # 定位登录按钮 是否可用
    #
    #     assert not self.page.login_and_sign_up_page.is_login_enabled()

        # assert not self.page.login_and_sign_up_page.is_login_enabled()

        #
        # if self.page.login_and_sign_up_page.is_login_enabled() == False:
        #     assert True
        # else:
        #     assert False

    @pytest.mark.parametrize("password", [random_password(), random_password()])
    def test_show_password(self, password):
        # 首页点击 我的
        self.page.home.click_mine()
        # 我的点击 登录注册
        self.page.mine.click_login_and_sign_up()
        # 登录注册输入 密码
        self.page.login_and_sign_up_page.input_password(password)

        # 判断 输入的密码找不到
        if not self.page.login_and_sign_up_page.is_password_exist(password):
            # 点击显示密码按钮
            self.page.login_and_sign_up_page.click_show_password()
            # 找到 输入的密码
            assert self.page.login_and_sign_up_page.is_password_exist(password)





