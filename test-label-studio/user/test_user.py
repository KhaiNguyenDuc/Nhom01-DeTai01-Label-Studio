import time

import pytest
from selenium.webdriver.common.by import By

from Utils.driver_connect import get_connection

def open_profile(driver):
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

    # Press account and setting
    account_btn = driver.find_element(By.XPATH, '//a[contains(@class, "ls-main-menu__item")][1]')
    account_btn.click()

def get_current_token(driver):
    # Get current token
    token_input = driver.find_element(By.XPATH, '//input[contains(@id, "access_token")]')
    current_token = token_input.get_attribute("value")
    return current_token

@pytest.mark.file_explorer
def test_update_account_info():
    driver = get_connection()

    open_profile(driver)

    # Update account info
    driver.find_element(By.NAME, "first_name").send_keys("Nguyễn Đức Khải")
    driver.find_element(By.NAME, "last_name").send_keys("Khải")
    driver.find_element(By.NAME, "phone").send_keys("0123456789")
    driver.find_element(By.XPATH, '//input[contains(@class, "file-input")]').send_keys(r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\avatar.jpg")
    save_btn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Save"]')
    save_btn.click()



def test_refresh_token():
    driver = get_connection()
    open_profile(driver)

    old_token = get_current_token(driver)
    # Press renew
    renew_btn = driver.find_element(By.NAME, "renew")
    renew_btn.click()
    # Get new token
    time.sleep(1)
    new_token = get_current_token(driver)

    assert old_token != new_token


