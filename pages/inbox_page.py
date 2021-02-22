from pages.base_page import BasePage
from locators.inbox_page import IboxPageLocators
from pages.create_new_message_page import CreateNewMessage


class InboxPage(BasePage):
    def create_a_new_message(self):
        self.element_search(IboxPageLocators.BUTTON_WRITE_MESSAGE).click()
        self.check_page_by_name("inbox")
        return CreateNewMessage(self.browser, self.browser.current_url)

    def log_out(self):
        self.element_search(IboxPageLocators.BUTTON_LOG_OUT).click()
