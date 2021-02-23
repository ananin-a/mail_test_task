from selenium.webdriver.common.by import By


class IboxPageLocators:
    """Локаторы страницы входящих сообщений"""

    BUTTON_WRITE_MESSAGE = (By.XPATH, '//span[@class="compose-button__wrapper"]')
    BUTTON_LOG_OUT = (By.XPATH, '//a[@id="PH_logoutLink"]')
