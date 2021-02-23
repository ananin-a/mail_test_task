from selenium.webdriver.common.by import By


class MessageSentPageLocators:
    """Локаторы страницы после отправки сообщения"""

    BUTTON_CLOSE_WINDOW = (By.XPATH, '//span[@tabindex="1000"]')
