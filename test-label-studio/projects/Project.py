from isodate import Duration
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v109 import browser
from selenium.webdriver.common.keys import Keys
import sys

from selenium.webdriver.support.wait import WebDriverWait


def test_create_project():

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press create project button
    driver.get("http://127.0.0.1:8080/projects/")
    driver.implicitly_wait(15)
    createProjectBtn = driver.find_element(By.CLASS_NAME, 'ls-button')
    createProjectBtn.click()

    # Enter value
    driver.find_element(By.NAME, "name").send_keys("test project")
    driver.find_element(By.NAME, "description").send_keys("test description")
    driver.implicitly_wait(15)
    saveProjectBtn = driver.find_element(By.XPATH,"//button[contains(@class, 'ls-button') and text()='Save']")
    saveProjectBtn.click()

def test_delete_project():

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press create project button
    driver.get("http://127.0.0.1:8080/projects/")
    driver.implicitly_wait(15)
    createProjectBtn = driver.find_element(By.CLASS_NAME, 'ls-button')
    createProjectBtn.click()

    # Enter value
    driver.find_element(By.NAME, "name").send_keys("test project")
    driver.find_element(By.NAME, "description").send_keys("test description")
    driver.implicitly_wait(15)
    saveProjectBtn = driver.find_element(By.XPATH,"//button[contains(@class, 'ls-button') and text()='Delete']")
    saveProjectBtn.click()





