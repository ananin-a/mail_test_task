from pages.base_page import BasePage
from pages.inbox_page import InboxPage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Главная страница"""

    def authorization_user(self, name: str, password: str):
        """Авторизовать пользователя"""
        self.check_page_by_name("mail")
        self.entry_user_name(name)
        self.click_entry_password_button()
        self.entry_user_password(password)
        self.click_enter_in_to_email()
        return InboxPage(self.browser, self.browser.current_url)

    def entry_user_name(self, name: str):
        """Ввести имя пользователя"""
        self.element_search(MainPageLocators.FIELD_USER_NAME).send_keys(name)

    def click_entry_password_button(self):
        """Нажать кнопку ввести пароль"""
        self.element_search(MainPageLocators.BUTTON_ENTRY_PASSWORD).click()

    def entry_user_password(self, password):
        """Ввести пароль пользователя"""
        self.element_search(MainPageLocators.FIELD_USER_PASSWORD).send_keys(password)

    def click_enter_in_to_email(self):
        """Нажать на кнопку войти в почтовый ящик"""
        self.element_search(MainPageLocators.BUTTON_ENTER_IN_TO_MAIL).click()
