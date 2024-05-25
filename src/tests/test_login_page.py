import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from pages.login_page import LoginPage
from utils.constants import (
    LOG_IN_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, FINALIZE_LOGIN_VIEW_GROUP,
    LOGIN_PAGE_VIEW_GROUP, PASSWORD_VIEW_GROUP, SIGNUP_VIEW_GROUP, NAME_INPUT,
    EMAIL_ALREADY_EXISTS_TOAST, WRONG_EMAIL_OR_PASSWORD_TOAST, CONFIRM_PASSWORD_INPUT,FINALIZE_SIGNUP_VIEW_GROUP
)

from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture
def mock_driver():
    return MagicMock()

@pytest.fixture
def login_page(mock_driver):
    return LoginPage(mock_driver)

def test_logging_in(login_page):
    with patch('pages.login_page.click_button') as mock_click_button, \
         patch('pages.login_page.enter_text') as mock_enter_text, \
         patch('pages.login_page.wait_for_toast_message') as mock_wait_for_toast:

        mock_wait_for_toast.return_value = False
        login_page.logging_in("test@example.com", "password")

        mock_click_button.assert_any_call(login_page.driver, AppiumBy.ANDROID_UIAUTOMATOR, LOG_IN_BUTTON)
        mock_enter_text.assert_any_call(login_page.driver, (AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_INPUT), "test@example.com")
        mock_enter_text.assert_any_call(login_page.driver, (AppiumBy.ANDROID_UIAUTOMATOR, PASSWORD_INPUT), "password")
        mock_click_button.assert_any_call(login_page.driver, AppiumBy.ANDROID_UIAUTOMATOR, FINALIZE_LOGIN_VIEW_GROUP)

def test_signing_up(login_page):
    with patch('pages.login_page.click_button') as mock_click_button, \
         patch('pages.login_page.enter_text') as mock_enter_text, \
         patch('pages.login_page.wait_for_toast_message') as mock_wait_for_toast, \
         patch('pages.login_page.navigate_back') as mock_navigate_back:
        
        mock_wait_for_toast.side_effect = [False, True]
        login_page.signing_up("test@example.com", "password", "testuser")

        mock_click_button.assert_any_call(login_page.driver, AppiumBy.ANDROID_UIAUTOMATOR, LOGIN_PAGE_VIEW_GROUP)
        mock_enter_text.assert_any_call(login_page.driver, (AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_INPUT), "test@example.com")
        mock_click_button.assert_any_call(login_page.driver, AppiumBy.ANDROID_UIAUTOMATOR, PASSWORD_VIEW_GROUP)
        mock_enter_text.assert_any_call(login_page.driver, (AppiumBy.ANDROID_UIAUTOMATOR, PASSWORD_INPUT), "password")
        mock_enter_text.assert_any_call(login_page.driver, (AppiumBy.ANDROID_UIAUTOMATOR, CONFIRM_PASSWORD_INPUT), "password")
        mock_click_button.assert_any_call(login_page.driver, AppiumBy.ANDROID_UIAUTOMATOR, SIGNUP_VIEW_GROUP)
        mock_enter_text.assert_any_call(login_page.driver, (AppiumBy.ANDROID_UIAUTOMATOR, NAME_INPUT), "testuser")
        mock_click_button.assert_any_call(login_page.driver, AppiumBy.ANDROID_UIAUTOMATOR, FINALIZE_SIGNUP_VIEW_GROUP)
