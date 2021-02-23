from pages.base_page import BasePage
from pages.message_sent_page import MessageSentPage
from locators.create_new_message_locators import CreateNewMessageLocators as CNMP
from constants.body_new_message import BodyNewMessage


class CreateNewMessage(BasePage):
    """Страница создания нового сообщения"""

    def fill_and_send_mail(self):
        """Заполнить все поля и отправить сообщение"""
        self.add_a_message_recipient()
        self.click_button_copy()
        self.add_a_copy_recipient()
        self.add_a_subject()
        self.add_a_body()
        self.click_send_message()
        return MessageSentPage(self.browser, self.browser.current_url)

    def add_a_message_recipient(self):
        """Добавить получателя"""
        self.element_search(CNMP.FIELD_SEND_EMAIL_TO).send_keys(BodyNewMessage.RECIPIENT_OF_MESSAGE)

    def click_button_copy(self):
        """Нажать на кнопку копия"""
        self.element_search(CNMP.BUTTON_COPY).click()

    def add_a_copy_recipient(self):
        """Заполнить поле копия получателю"""
        self.element_search(CNMP.FIELD_SEND_COPY_EMAIL).send_keys(BodyNewMessage.EMAIL_COPY)

    def add_a_subject(self):
        """Добавить темо письма"""
        self.element_search(CNMP.FIELD_EMAIL_SUBJECT).send_keys(BodyNewMessage.EMAIL_SUBJECT)

    def add_a_body(self):
        """Заполнить тело письма"""
        self.element_search(CNMP.FIELD_THE_BODY_MESSAGE).send_keys(BodyNewMessage.EMAIL_BODY)

    def click_send_message(self):
        """Нажать отправить сообщение"""
        self.element_search(CNMP.BUTTON_SEND_MESSAGE).click()
