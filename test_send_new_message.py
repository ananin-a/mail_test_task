from pages.main_page import MainPage
from constants.url import URL

def test_send_a_new_message(browser):
    main_page = MainPage(browser, URL)
    main_page.open()

    login_page = main_page.click_sing_in(browser)
