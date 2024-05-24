from appium import webdriver
from appium.options.android import UiAutomator2Options
import json
import os
from dotenv import load_dotenv
import logging
from typing import Optional

load_dotenv()

class DriverManager:
    def __init__(self):
        self.driver: Optional[webdriver.Remote] = None

    def initialize_driver(self) -> webdriver.Remote:
        """Initializes the Appium WebDriver."""
        try:
            with open('config/capabilities.json') as f:
                capabilities = json.load(f)

            capabilities['appPackage'] = os.getenv('APP_PACKAGE')
            options = UiAutomator2Options().load_capabilities(capabilities)

            self.driver = webdriver.Remote(os.getenv('APPIUM_SERVER_URL'), options=options)
            logging.info("WebDriver initialized successfully")
        except Exception as e:
            logging.error("Error initializing WebDriver: %s", e)
            raise
        return self.driver

    def get_driver(self) -> webdriver.Remote:
        """Returns the WebDriver instance, initializing it if necessary."""
        if not self.driver:
            self.initialize_driver()
        return self.driver

    def quit_driver(self):
        """Quits the WebDriver instance."""
        if self.driver:
            self.driver.quit()
            self.driver = None
            logging.info("WebDriver quit successfully")
