import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from typing import Tuple, Any

from typing import Optional
import time 

# Assuming the retry function is within src/utils/retry.py
from utils.retry import retry

import logging 
import json
import os

from dotenv import load_dotenv

load_dotenv()



def click_button(driver: WebDriver, by: By, value: str, timeout: int = 20):
    """Waits for an element to be clickable and clicks it."""
    def action():
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        logging.info(f"Clicked element located by {by} with value {value}")
    
    retry(action)

def send_text(driver: WebDriver, by: By, value: str, keys: str, timeout: int = 20):
    """Waits for an element to be clickable and sends keys to it."""
    def action():
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.send_keys(keys)
        logging.info(f"Sent keys '{keys}' to element located by {by} with value {value}")
    
    retry(action)

def enter_text(driver: WebDriver, selector: Tuple[By, str], text: str, timeout: int = 10):
    """Waits for a text input element to be visible and enters text."""
    def action():
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(selector)
        )
        element.clear()
        element.send_keys(text)
        logging.info(f"Entered text '{text}' into element with selector {selector}")
    
    retry(action)

def wait_for_toast_message(driver: WebDriver, selector: Tuple[By, str], timeout: int = 10) -> bool:
    """Waits for a toast message to appear."""
    #def action():
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(selector)
        )
        logging.info(f"Toast message with selector {selector} found")
        return True 

        print("None",selector)
        #return retry(action)
    except TimeoutException:
        logging.warning(f"No toast message with selector {selector} found within the given time")
        return False

def navigate_back(driver: WebDriver, timeout: int = 10) -> any:
    """Navigates back using the Android back button."""
    #def action():
    try:
        driver.back()
        logging.info("Back button pressed successfully")
        return True
        #return retry(action)
    except TimeoutException:
        logging.warning("Back button element not found within the given time")
        return False

def getActivity () -> any:
    try:
        activity = os.getenv('APP_ACTIVITY')
        return activity
    except Exception as e:
        return "error" 



def close_app(driver: WebDriver): #def close_app(driver: WebDriver, app_package: str):
    """Closes the app."""
    app_package = 'com.gtschoolapp'
    logging.info("Closing the app")
    driver.terminate_app(app_package)

def reopen_app(driver: WebDriver): #def reopen_app(driver: WebDriver, app_package: str):
    """Reopens the app."""
    app_package = 'com.gtschoolapp'
    logging.info("Reopening the app")
    driver.activate_app(app_package)
