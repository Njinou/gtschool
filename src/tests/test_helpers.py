import pytest
import sys
import os
from unittest.mock import MagicMock, patch

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from selenium.webdriver.common.by import By

from appium.webdriver.common.appiumby import AppiumBy

from utils.helpers import click_button, send_text, enter_text, wait_for_toast_message, navigate_back
from utils.constants import (
    EMAIL_INPUT, PASSWORD_INPUT, LOG_IN_BUTTON, FINALIZE_LOGIN_VIEW_GROUP
)

@pytest.fixture
def mock_driver():
    return MagicMock()

def test_click_button(mock_driver):
    with patch('utils.helpers.WebDriverWait') as mock_wait:
        mock_element = MagicMock()
        mock_wait.return_value.until.return_value = mock_element

        click_button(mock_driver, AppiumBy.ANDROID_UIAUTOMATOR, LOG_IN_BUTTON)

        mock_element.click.assert_called_once()

def test_send_text(mock_driver):
    with patch('utils.helpers.WebDriverWait') as mock_wait:
        mock_element = MagicMock()
        mock_wait.return_value.until.return_value = mock_element

        send_text(mock_driver, AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_INPUT, 'test_value')

        mock_element.send_keys.assert_called_once_with('test_value')

def test_enter_text(mock_driver):
    with patch('utils.helpers.WebDriverWait') as mock_wait:
        mock_element = MagicMock()
        mock_wait.return_value.until.return_value = mock_element

        enter_text(mock_driver, (AppiumBy.ANDROID_UIAUTOMATOR, EMAIL_INPUT), 'test_value')

        mock_element.clear.assert_called_once()
        mock_element.send_keys.assert_called_once_with('test_value')

def test_wait_for_toast_message(mock_driver):
    with patch('utils.helpers.WebDriverWait') as mock_wait:
        print ("assert in wait for toast line 52 ")
        result = wait_for_toast_message(mock_driver, (AppiumBy.ANDROID_UIAUTOMATOR, LOG_IN_BUTTON))

        assert result is True

def test_navigate_back(mock_driver):
    with patch('utils.helpers.WebDriverWait') as mock_wait:
        result = navigate_back(mock_driver)
        print("asserting in navigate back for toast line 60")
        assert result is True
