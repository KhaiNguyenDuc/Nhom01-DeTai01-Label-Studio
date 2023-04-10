from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_success():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("http://127.0.0.1:8080/user/login/")

    driver.find_element(By.NAME,"email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME,"password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
    loginBtn.click()
    driver.close()

def test_login_failure():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("http://127.0.0.1:8080/user/login/")

    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k123")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()

    errorTxt = driver.find_element(By.CLASS_NAME, "error")

    assert errorTxt.text == "The email and password you entered don't match."
    driver.close()