from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from time import sleep


def test_send_a_new_message(browser):
    main_page = MainPage(browser, MainPageLocators.URL)
    main_page.open()
    inbox_page = main_page.authorization_user(browser)

    new_message = inbox_page.create_a_new_message(browser)
    new_message.fill_out_and_send_a_mail()
