from selenium.webdriver.common.by import By


class MainPage:
    """Locators on the main page"""
    BUTTON_LOG_IN_TO_MAIL = (By.XPATH, '//a[@href="https://account.mail.ru/login?from=main"]')


class LoginPage:
    """Locators on the login page"""
    FIELD_USER_NAME = (By.XPATH, '//input[@name="username"]')
    FIELD_USER_PASSWORD = (By.XPATH, '//input[@name="password"]')
    BUTTON_ENTRY_PASSWORD = (By.XPATH, '//button[@data-test-id="next-button"]')
    BUTTON_ENTER_IN_TO_MAIL = (By.XPATH, '//button[@data-test-id="submit-button"]')


class InboxMailPage:
    """Locators on the incoming message page"""
    BUTTON_WRITE_MESSAGE = (By.XPATH, '//span[@class="compose-button__wrapper"]')


class PopUpNewMessage:
    """Locators in the new message pop-up window"""
    FIELD_SEND_EMAIL_TO = (By.XPATH, '//input[@tabindex="100"]')
    FIELD_SEND_COPY_EMAIL = (By.XPATH, '//input[@tabindex="200"]')
    FIELD_EMAIL_SUBJECT = (By.XPATH, '//input[@name="Subject"]')
    FIELD_THE_BODY_MESSAGE = (By.XPATH, '//div[@role="textbox"]')
    BUTTON_COPY = (By.XPATH, '//button[@tabindex="720"]')
    BUTTON_SEND_MESSAGE = (By.XPATH, '//span[@tabindex="570"]')
