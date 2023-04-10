from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_signup_success():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("http://127.0.0.1:8080/user/signup")

    driver.find_element(By.NAME,"email").send_keys("duckhai12345@gmail.com")
    driver.find_element(By.NAME,"password").send_keys("k989898k123")
    signupBtn = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
    signupBtn.click()
    driver.close()

def test_email_invalid():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("http://127.0.0.1:8080/user/signup")

    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k123")
    signupBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    signupBtn.click()

    error =  driver.find_element(By.CLASS_NAME, "field_errors")

    assert error.text == "User with this email already exists"
    driver.close()


def test_password_invalid():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("http://127.0.0.1:8080/user/signup")

    driver.find_element(By.NAME, "email").send_keys("duckhai123@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("1")
    signupBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    signupBtn.click()

    error = driver.find_element(By.CLASS_NAME, "field_errors")

    assert error.text == "Please enter a password 8-12 characters in length"
    driver.close()


