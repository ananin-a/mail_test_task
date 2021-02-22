from selenium.webdriver.common.by import By


class MainPageLocators:
    """Locators on the main page"""
    URL = "https://mail.ru/"

    FIELD_USER_NAME = (By.XPATH, '//input[@name="login"]')
    FIELD_USER_PASSWORD = (By.XPATH, '//input[@name="password"]')
    BUTTON_ENTRY_PASSWORD = (By.XPATH, '//button[@data-testid="enter-password"]')
    BUTTON_ENTER_IN_TO_MAIL = (By.XPATH, '//button[@data-testid="login-to-mail"]')
