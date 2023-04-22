import pytest
from selenium.webdriver.common.by import By
from Utils.driver_connect import get_connection

def test_logout():
    driver = get_connection()
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press user profile
    user_profile = driver.find_element(By.XPATH, '//div[contains(@class, "ls-userpic")]')
    user_profile.click()

    # Press logout
    logout_btn = driver.find_element(By.XPATH, '//ul[contains(@class, "ls-main-menu")]/li[2]')
    logout_btn.click()