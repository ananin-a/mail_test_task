from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Базовые методы"""

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Открыть страницу"""
        self.browser.get(self.url)

    def element_search(self, locator: str, timeout: int = 5):
        """
        Поиск элемента на странице с явным ожиданием

        :param locator: String
        :param timeout: Int
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(
                locator), message=f">>> Невозможно найт элемент по данному локатору: {locator}")

    def check_page_by_name(self, name_page: str, timeout: int = 5):
        """
        Проверка на правильность нахождения с не явным ожиданием

        :param name_page: String
        :param timeout: Int
        """
        self.browser.implicitly_wait(timeout)
        assert name_page in self.browser.current_url, f">>> Вы находитесь не на той странице {name_page} page"
