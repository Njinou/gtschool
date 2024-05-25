import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from drivers.driver import DriverManager

@pytest.fixture(scope='session')
def driver_manager():
    manager = DriverManager()
    yield manager
    manager.quit_driver()

@pytest.fixture(scope='session')
def driver(driver_manager):
    return driver_manager.get_driver()
