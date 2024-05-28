
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import time 
from utils.constants import (NAVIGATE_EXPLORE)
from pages.base_page import BasePage
from utils.helpers import click_button
from selenium.webdriver.common.by import By

from appium.webdriver.common.appiumby import AppiumBy

import logging

class PlayPage(BasePage):
    def play_course_units(self, courses: str, play: str):
        """playing the courses."""
        logging.info("Attempting to play the courses")
        try:
            click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, NAVIGATE_EXPLORE)
            time.sleep(1)
            click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, courses)
            time.sleep(1)
            print("navigating to the explore tab")
            click_button(self.driver, AppiumBy.ANDROID_UIAUTOMATOR, play)
            time.sleep(15)
        except Exception as e:
            logging.error(f"Error  in: {courses} {e} ")