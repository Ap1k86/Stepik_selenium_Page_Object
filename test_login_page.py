from .pages.login_page import LoginPage


# Метод проверки корректности url адреса.
def test_quest_should_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


# Метод проверки наличия формы логина.
def test_quest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


# Метод проверки наличия формы регистрации.
def test_quest_should_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
