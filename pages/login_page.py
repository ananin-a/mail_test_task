from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_a_page_title(self, title):
        text = self.element_search(LoginPageLocators.TITLE_LOGIN_PAGE).text
        assert text == title, \
            ">>> This is not LoginPage"
