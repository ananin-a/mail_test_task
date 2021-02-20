from pages.base_page import BasePage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Main Page"""

    def click_sing_in(self, browser) -> LoginPage:
        """
        Go to login page

        :return: LoginPage
        """
        self.element_search(MainPageLocators.BUTTON_LOG_IN_TO_MAIL).click()

        return LoginPage(browser, browser.current_url)

    def should_be_a_page_title(self, title):
        text = self.element_search(MainPageLocators.BUTTON_LOG_IN_TO_MAIL).text
        assert text == title, \
            ">>> This is not MainPage"
