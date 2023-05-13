import pytest

from Utils.driver_connect import get_connection
from run_first import test_init_data

@pytest.fixture(scope="session", autouse=True)
def init_data():
    print('a')
    driver = get_connection()
    test_init_data(driver)
    driver.close()

