from pages.base_page import BasePage
from pages.message_sent_page import MessageSentPage
from locators.create_new_message_locators import CreateNewMessageLocators as CNMP


class CreateNewMessage(BasePage):
    """Страница создания нового сообщения"""

    def fill_and_send_mail(self, recipient: str, copy_address: str, email_subject: str, email_body: str):
        """Заполнить все поля и отправить сообщение"""
        self.add_a_message_recipient(recipient)
        self.click_button_copy()
        self.add_a_copy_recipient(copy_address)
        self.add_a_subject(email_subject)
        self.add_a_body(email_body)
        self.click_send_message()
        return MessageSentPage(self.browser, self.browser.current_url)

    def add_a_message_recipient(self, recipient: str):
        """Добавить получателя"""
        self.element_search(CNMP.FIELD_SEND_EMAIL_TO).send_keys(recipient)

    def click_button_copy(self):
        """Нажать на кнопку копия"""
        self.element_search(CNMP.BUTTON_COPY).click()

    def add_a_copy_recipient(self, copy_address: str):
        """Заполнить поле копия получателю"""
        self.element_search(CNMP.FIELD_SEND_COPY_EMAIL).send_keys(copy_address)

    def add_a_subject(self, email_subject: str):
        """Добавить тему письма"""
        self.element_search(CNMP.FIELD_EMAIL_SUBJECT).send_keys(email_subject)

    def add_a_body(self, email_body: str):
        """Заполнить тело письма"""
        self.element_search(CNMP.FIELD_THE_BODY_MESSAGE).send_keys(email_body)

    def click_send_message(self):
        """Нажать отправить сообщение"""
        self.element_search(CNMP.BUTTON_SEND_MESSAGE).click()
