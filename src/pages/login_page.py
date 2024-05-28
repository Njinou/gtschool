
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import time 

from pages.base_page import BasePage
from utils.helpers import click_button, enter_text, send_text, wait_for_toast_message, navigate_back
from utils.constants import (
    LOG_IN_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, CONFIRM_PASSWORD_INPUT, NAME_INPUT, 
    EMAIL_ALREADY_EXISTS_TOAST, WRONG_EMAIL_OR_PASSWORD_TOAST, LOGIN_PAGE_VIEW_GROUP, ERROR,
    PASSWORD_VIEW_GROUP, SIGNUP_VIEW_GROUP, FINALIZE_SIGNUP_VIEW_GROUP, 
    BACK_BUTTON_PATH_VIEW, FINALIZE_LOGIN_VIEW_GROUP
)
from selenium.webdriver.common.by import By

from appium.webdriver.common.appiumby import AppiumBy


import logging

class LoginPage(BasePage):
    def logging_in(self, email: str, password: str):
        """Logs in using the provided email and password."""
        logging.info("Attempting to log in")
        try:
            click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, LOG_IN_BUTTON)
            click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, LOGIN_PAGE_VIEW_GROUP)
            enter_text(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_INPUT), email)
            enter_text(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, PASSWORD_INPUT), password)
            click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, FINALIZE_LOGIN_VIEW_GROUP) 

            if  wait_for_toast_message(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, WRONG_EMAIL_OR_PASSWORD_TOAST)):
                logging.warning("Verify either the email or the password or sign up.")
            elif wait_for_toast_message(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, ERROR)): 
                print("error Logging in  went totally wrong despite credentials being well vetted !!! bug !!!!!!!!!!!!!!")
            else:
                logging.info("Log In successful!")
                time.sleep(5)
        except Exception as e:
            logging.error(f"Error logging in: {e}")

    def signing_up(self, email: str, password: str, name: str):
        """Signs up a new user with the provided email, password, and name."""
        logging.info("Attempting to sign up")
        try:
            click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, LOGIN_PAGE_VIEW_GROUP)
            enter_text(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_INPUT), email)
            click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, PASSWORD_VIEW_GROUP)
            email_exist = wait_for_toast_message(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_ALREADY_EXISTS_TOAST))
            if not email_exist:
                enter_text(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, PASSWORD_INPUT), password)
                enter_text(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, CONFIRM_PASSWORD_INPUT), password)
                click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, SIGNUP_VIEW_GROUP)
                enter_text(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, NAME_INPUT), name)
                print("finalizing it and not knowing why It does not work ")
                click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, FINALIZE_SIGNUP_VIEW_GROUP)
                error_auth = wait_for_toast_message(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, ERROR))
                if error_auth:
                    print("error signing up !!! bug !!!!!!!!!!!!!!")
                time.sleep(5)
            else:
                Loggin_in_exist = wait_for_toast_message(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, LOG_IN_BUTTON))
                while not Loggin_in_exist:
                    navigate_back(self.driver)
                    Loggin_in_exist = wait_for_toast_message(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR, LOG_IN_BUTTON))
                self.logging_in(email, password)
        except Exception as e:
            logging.error(f"Error signing up: {e}")
