import logging
from src.drivers.driver import DriverManager
from src.pages.login_page import LoginPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    driver_manager = DriverManager()
    driver = driver_manager.get_driver()
    login_page = LoginPage(driver)

    try:
        login_page.signing_up("billbur4332kjrpp@gmail.com", "P@ssw0rd", "nameee1245")
    finally:
        driver_manager.quit_driver()
