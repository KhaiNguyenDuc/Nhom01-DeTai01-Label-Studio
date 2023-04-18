from selenium.webdriver.common.by import By
from Utils.driver_connect import get_connection


def test_login_success():
    driver = get_connection()

    driver.get("http://127.0.0.1:8080/user/login/")

    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()


def test_login_failure():
    driver = get_connection()

    driver.get("http://127.0.0.1:8080/user/login/")

    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k123")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()

    errorTxt = driver.find_element(By.CLASS_NAME, "error")

    assert errorTxt.text == "The email and password you entered don't match."