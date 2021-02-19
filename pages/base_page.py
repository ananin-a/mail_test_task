from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Open page"""
        self.browser.get(self.url)

    def element_search_on_the_page(self, locator, timeout: int = 3):
        """
        Поиск элемента с явным ожиданием.
        :param locator: локатор
        :param timeout: время явного ожидания
        :return: WebDriverWait
        """
        return WDW(self.browser, timeout).until(
            EC.presence_of_element_located(
                locator
            ), message=f">>> It is impossible to find an element locator: {locator}"
        )
