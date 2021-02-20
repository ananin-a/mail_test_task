from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Locators on the login page"""
    FIELD_USER_NAME = (By.XPATH, '//input[@name="username"]')
    FIELD_USER_PASSWORD = (By.XPATH, '//input[@name="password"]')
    BUTTON_ENTRY_PASSWORD = (By.XPATH, '//button[@data-test-id="next-button"]')
    BUTTON_ENTER_IN_TO_MAIL = (By.XPATH, '//button[@data-test-id="submit-button"]')

    TITLE_LOGIN_PAGE = (By.XPATH, '//h2[@class]')
