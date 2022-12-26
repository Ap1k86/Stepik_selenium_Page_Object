from .base_page import BasePage
from .locators import LoginPageLocators
"""    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"
"""


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # реализуйте проверку на корректный url адрес
    def should_be_login_url(self):
        assert "/login" in self.open(), "login is absent in current url"

    # реализуйте проверку, что есть форма логина
    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # реализуйте проверку, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


"""
Передаю свои знания людям из будущего, чтобы они не тупили как я.
Вам надо:
1) Файл с шаблоном использовать по аналогии с main_page файлом из прошлых заданий и туда напихать проверок
2) Создать файл аналог test_main_page из прошлых заданий, но с уже новыми тестами
3) Ссылку использовать уже на страницу логина http://selenium1py.pythonanywhere.com/ru/accounts/login/
4) Дальше по инструкции в задании
"""
