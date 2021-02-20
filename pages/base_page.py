from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Open page"""
        self.browser.get(self.url)

    def element_search(self, locator: str, timeout: int = 5):
        """
        Search for an element with an explicit expectation

        :param locator: locator
        :param timeout: explicit waiting time
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(
                locator
            ), message=f">>> It is impossible to find an element locator: {locator}"
        )
