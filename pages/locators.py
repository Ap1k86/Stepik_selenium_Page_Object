from selenium.webdriver.common.by import By


# Класс поиска ссылок для файла "main_page.py".
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


# Класс поиска ссылок для файла "login_page.py".
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
