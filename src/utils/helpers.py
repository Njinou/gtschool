import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from typing import Tuple, Any
from src.utils.retry import retry

def click_button(driver: WebDriver, by: By, value: str, timeout: int = 10):
    """Waits for an element to be clickable and clicks it."""
    def action():
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        logging.info(f"Clicked element located by {by} with value {value}")
    
    retry(action)

def send_text(driver: WebDriver, by: By, value: str, keys: str, timeout: int = 10):
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
    def action():
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(selector)
        )
        logging.info(f"Toast message with selector {selector} found")
        return True
    
    try:
        return retry(action)
    except TimeoutException:
        logging.warning(f"No toast message with selector {selector} found within the given time")
        return False

def navigate_back(driver: WebDriver, timeout: int = 10) -> bool:
    """Navigates back using the Android back button."""
    def action():
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(('new UiSelector().className("com.horcrux.svg.PathView")'))
        )
        driver.back()
        logging.info("Back button pressed successfully")
        return True

    try:
        return retry(action)
    except TimeoutException:
        logging.warning("Back button element not found within the given time")
        return False
