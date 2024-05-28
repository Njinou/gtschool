import pytest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from drivers.driver import DriverManager
from utils.helpers import close_app, reopen_app

@pytest.fixture
def driver_manager():
    return DriverManager()

def test_initialize_driver(driver_manager):
    with patch('drivers.driver.webdriver.Remote') as mock_remote, \
         patch('drivers.driver.load_dotenv'), \
         patch('drivers.driver.os.getenv') as mock_getenv:
        mock_driver = MagicMock()
        mock_remote.return_value = mock_driver
        mock_getenv.side_effect = lambda key: {
            'APPIUM_SERVER_URL': 'http://localhost:4723/wd/hub',
            'APP_PACKAGE': 'com.gtschoolapp'
        }.get(key)

        driver = driver_manager.initialize_driver()

        assert driver == mock_driver
        assert driver_manager.driver == mock_driver

def test_get_driver_initializes_if_none(driver_manager):
    with patch('drivers.driver.webdriver.Remote') as mock_remote, \
         patch('drivers.driver.load_dotenv'), \
         patch('drivers.driver.os.getenv') as mock_getenv:
        mock_driver = MagicMock()
        mock_remote.return_value = mock_driver
        mock_getenv.side_effect = lambda key: {
            'APPIUM_SERVER_URL': 'http://localhost:4723/wd/hub',
            'APP_PACKAGE': 'com.gtschoolapp'
        }.get(key)

        driver = driver_manager.get_driver()

        assert driver == mock_driver
        assert driver_manager.driver == mock_driver

def test_get_driver_returns_existing(driver_manager):
    with patch('drivers.driver.webdriver.Remote'):
        mock_driver = MagicMock()
        driver_manager.driver = mock_driver
        
        driver = driver_manager.get_driver()

        assert driver == mock_driver
        assert driver_manager.driver == mock_driver

def test_quit_driver(driver_manager):
    mock_driver = MagicMock()
    driver_manager.driver = mock_driver
    
    driver_manager.quit_driver()

    mock_driver.quit.assert_called_once()
    assert driver_manager.driver is None

"""def test_close_and_reopen_app(driver):
    app_package = 'com.gtschoolapp'
    app_activity = '.MainActivity'
    
    # Close the app
    close_app(driver)
    
    # Reopen the app
    reopen_app(driver, app_package, app_activity)
    
    # Perform an assertion or verification after reopening the app
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Welcome")'))
    )
    assert element is not None"""
