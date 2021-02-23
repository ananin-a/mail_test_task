from selenium.webdriver.common.by import By


class CreateNewMessageLocators:
    """Локаторы странцицы создания нового сообщения"""

    FIELD_SEND_EMAIL_TO = (By.XPATH, '//div//input[@tabindex="100"]')
    FIELD_SEND_COPY_EMAIL = (By.XPATH, '//input[@tabindex="200"]')
    FIELD_EMAIL_SUBJECT = (By.XPATH, '//input[@name="Subject"]')
    FIELD_THE_BODY_MESSAGE = (By.XPATH, '//div[@role="textbox"]')

    BUTTON_COPY = (By.XPATH, '//button[@tabindex="720"]')
    BUTTON_SEND_MESSAGE = (By.XPATH, '//span[@tabindex="570"]')
