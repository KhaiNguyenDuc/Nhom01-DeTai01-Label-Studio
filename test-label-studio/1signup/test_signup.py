import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils.driver_connect import get_connection

@pytest.mark.order(1)
def test_signup_success():
    driver = get_connection()

    driver.get("http://127.0.0.1:8080/user/signup")

    driver.find_element(By.NAME,"email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME,"password").send_keys("k989898k")
    signupBtn = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
    signupBtn.click()

@pytest.mark.order(2)
def test_email_invalid():
    driver = get_connection()

    driver.get("http://127.0.0.1:8080/user/signup")

    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    signupBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    signupBtn.click()

    driver.implicitly_wait(25)
    error = driver.find_element(By.CLASS_NAME, "field_errors")

    assert error.text == "User with this email already exists"

@pytest.mark.order(3)
def test_password_invalid():
    driver = get_connection()

    driver.get("http://127.0.0.1:8080/user/signup")

    driver.find_element(By.NAME, "email").send_keys("duckhailinux12@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("1")
    signupBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    signupBtn.click()

    error = driver.find_element(By.CLASS_NAME, "field_errors")

    assert error.text == "Please enter a password 8-12 characters in length"


