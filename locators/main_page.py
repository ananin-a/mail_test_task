from selenium.webdriver.common.by import By


class MainPage:
    """Locators on the main page"""
    BUTTON_LOG_IN_TO_MAIL = (By.XPATH, '//a[@href="https://account.mail.ru/login?from=main"]')
