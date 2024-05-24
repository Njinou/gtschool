from src.pages.base_page import BasePage
from src.utils.helpers import click_button, enter_text, send_text, wait_for_toast_message, navigate_back
from src.utils.constants import (
    LOG_IN_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, CONFIRM_PASSWORD_INPUT, NAME_INPUT, 
    EMAIL_ALREADY_EXISTS_TOAST, WRONG_EMAIL_OR_PASSWORD_TOAST, LOGIN_PAGE_VIEW_GROUP, 
    PASSWORD_VIEW_GROUP, SIGNUP_VIEW_GROUP, FINALIZE_SIGNUP_VIEW_GROUP, 
    BACK_BUTTON_PATH_VIEW, FINALIZE_LOGIN_VIEW_GROUP
)
from selenium.webdriver.common.by import By
import logging

class LoginPage(BasePage):
    def logging_in(self, email: str, password: str):
        """Logs in using the provided email and password."""
        logging.info("Attempting to log in")
        try:
            click_button(self.driver, By.ANDROID_UIAUTOMATOR, LOG_IN_BUTTON)
            click_button(self.driver, By.ANDROID_UIAUTOMATOR, LOGIN_PAGE_VIEW_GROUP)
            enter_text(self.driver, (By.ANDROID_UIAUTOMATOR, EMAIL_INPUT), email)
            enter_text(self.driver, (By.ANDROID_UIAUTOMATOR, PASSWORD_INPUT), password)

            if not wait_for_toast_message(self.driver, (By.ANDROID_UIAUTOMATOR, WRONG_EMAIL_OR_PASSWORD_TOAST)):
                logging.info("Log In successful!")
                click_button(self.driver, By.ANDROID_UIAUTOMATOR, FINALIZE_LOGIN_VIEW_GROUP)
            else:
                logging.warning("Verify either the email or the password or sign up.")
        except Exception as e:
            logging.error(f"Error logging in: {e}")

    def signing_up(self, email: str, password: str, name: str):
        """Signs up a new user with the provided email, password, and name."""
        logging.info("Attempting to sign up")
        try:
            click_button(self.driver, By.ANDROID_UIAUTOMATOR, LOGIN_PAGE_VIEW_GROUP)
            enter_text(self.driver, (By.ANDROID_UIAUTOMATOR, EMAIL_INPUT), email)
            click_button(self.driver, By.ANDROID_UIAUTOMATOR, PASSWORD_VIEW_GROUP)

            if not wait_for_toast_message(self.driver, (By.ANDROID_UIAUTOMATOR, EMAIL_ALREADY_EXISTS_TOAST)):
                enter_text(self.driver, (By.ANDROID_UIAUTOMATOR, PASSWORD_INPUT), password)
                enter_text(self.driver, (By.ANDROID_UIAUTOMATOR, CONFIRM_PASSWORD_INPUT), password)
                click_button(self.driver, By.ANDROID_UIAUTOMATOR, SIGNUP_VIEW_GROUP)
                enter_text(self.driver, (By.ANDROID_UIAUTOMATOR, NAME_INPUT), name)
                click_button(self.driver, By.ANDROID_UIAUTOMATOR, FINALIZE_SIGNUP_VIEW_GROUP)
                time.sleep(10)
            else:
                while not wait_for_toast_message(self.driver, (By.ANDROID_UIAUTOMATOR, LOG_IN_BUTTON)):
                    navigate_back(self.driver)
                self.logging_in(email, password)
        except Exception as e:
            logging.error(f"Error signing up: {e}")
