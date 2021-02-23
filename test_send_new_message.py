from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from constants.user_authorization_data import UserAuthorizationData
from constants.body_new_message import BodyNewMessage


def test_send_a_new_message(browser):
    """Отправка нового сообщения"""

    # Данные польователя
    user_name = UserAuthorizationData.USER_NAME
    user_password = UserAuthorizationData.USER_PASSWORD

    # Тело письма
    recipient = BodyNewMessage.RECIPIENT_OF_MESSAGE
    copy_address = BodyNewMessage.EMAIL_COPY
    email_subject = BodyNewMessage.EMAIL_SUBJECT
    email_body = BodyNewMessage.EMAIL_BODY

    main_page = MainPage(browser, MainPageLocators.URL)
    main_page.open()
    inbox_page = main_page.authorization_user(user_name, user_password)
    new_message = inbox_page.create_a_new_message()
    sent_message_page = new_message.fill_and_send_mail(recipient, copy_address, email_subject, email_body)
    sent_message_page.close_sent_message_page()
    inbox_page.log_out()
