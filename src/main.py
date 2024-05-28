import sys
import os
import logging
import time 
# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from drivers.driver import DriverManager
from pages.login_page import LoginPage
from pages.play_courses_page import PlayPage
from utils.helpers  import close_app,reopen_app
from utils.constants import (DISPLAY_HIGH_SCHOOL_COURSES,PLAY_HIGH_SCHOOL_COURSES)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()
    login_page = LoginPage(driver)
    play_page = PlayPage(driver)

    try:
        login_page.logging_in("nitcheupascal@gmail.com", "P@ssw0rd") #, "nameee1245"
        close_app(driver)
        reopen_app(driver)
        time.sleep(3)
        play_page.play_course_units(DISPLAY_HIGH_SCHOOL_COURSES,PLAY_HIGH_SCHOOL_COURSES)
        time.sleep(10)
    finally:
        driver_manager.quit_driver()
