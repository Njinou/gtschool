import sys
import os
import logging

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from drivers.driver import DriverManager
from pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()
    login_page = LoginPage(driver)

    try:
        login_page.signing_up("12311434334mbouendeu@gmail.com", "P@ssw0rd","queueee") #, "nameee1245"
    finally:
        driver_manager.quit_driver()
