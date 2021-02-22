from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


def test_send_a_new_message(browser):
    main_page = MainPage(browser, MainPageLocators.URL)
    main_page.open()

    inbox_page = main_page.authorization_user()
    new_message = inbox_page.create_a_new_message()
    sent_message_page = new_message.fill_and_send_mail()
    sent_message_page.close_sent_message_page()
    inbox_page.log_out()
