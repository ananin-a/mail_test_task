from pages.base_page import BasePage
from pages.message_sent_page import MessageSentPage
from locators.create_new_message_page_locators import CreateNewMessagePageLocators as CNMP
from constants.email_body import EmailBody


class CreateNewMessage(BasePage):

    def add_a_message_recipient(self):
        text_field = self.element_search(CNMP.FIELD_SEND_EMAIL_TO)
        text_field.send_keys(EmailBody.RECIPIENT_OF_MESSAGE)

    def click_button_copy(self):
        self.element_search(CNMP.BUTTON_COPY).click()

    def add_a_copy_recipient(self):
        self.element_search(CNMP.FIELD_SEND_COPY_EMAIL).send_keys(EmailBody.EMAIL_COPY)

    def add_a_subject(self):
        self.element_search(CNMP.FIELD_EMAIL_SUBJECT).send_keys(EmailBody.EMAIL_SUBJECT)

    def add_a_body(self):
        self.element_search(CNMP.FIELD_THE_BODY_MESSAGE).send_keys(EmailBody.EMAIL_BODY)

    def click_send_message(self):
        self.element_search(CNMP.BUTTON_SEND_MESSAGE).click()

    def fill_and_send_mail(self):
        self.add_a_message_recipient()
        self.click_button_copy()
        self.add_a_copy_recipient()
        self.add_a_subject()
        self.add_a_body()
        self.click_send_message()
        return MessageSentPage(self.browser, self.browser.current_url)
