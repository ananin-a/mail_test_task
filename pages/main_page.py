from pages.base_page import BasePage
from pages.inbox_page import InboxPage
from locators.main_page_locators import MainPageLocators
from constants.user_data import UserData


class MainPage(BasePage):
    def entry_user_name(self):
        self.element_search(MainPageLocators.FIELD_USER_NAME).send_keys(UserData.USER_NAME)

    def click_entry_password_button(self):
        self.element_search(MainPageLocators.BUTTON_ENTRY_PASSWORD).click()

    def entry_user_password(self):
        self.element_search(MainPageLocators.FIELD_USER_PASSWORD).send_keys(UserData.USER_PASSWORD)

    def click_enter_in_to_email(self):
        self.element_search(MainPageLocators.BUTTON_ENTER_IN_TO_MAIL).click()

    def authorization_user(self):
        self.check_page_by_name("mail")
        self.entry_user_name()
        self.click_entry_password_button()
        self.entry_user_password()
        self.click_enter_in_to_email()
        return InboxPage(self.browser, self.browser.current_url)
