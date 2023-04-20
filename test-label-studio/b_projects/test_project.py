import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils.driver_connect import get_connection

def open_general_setting(driver):
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press project button
    driver.implicitly_wait(15)
    first_button = driver.find_element(By.XPATH, "//button[contains(@class, 'ls-button_withIcon')]")
    first_button.click()

    # Press setting
    driver.implicitly_wait(15)
    settings_link = driver.find_element(By.XPATH, '//a[contains(@class, "ls-main-menu__item") and text()="Settings"]')
    settings_link.click()



def test_create_project():

    driver = get_connection()

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

    driver.close()

def test_delete_project():

    driver = get_connection()

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
    driver.close()

def test_config_project():
    driver = get_connection()
    open_general_setting(driver)

    driver.find_element(By.XPATH, '//input[contains(@name, "title")]').send_keys("This is title of project")
    driver.find_element(By.XPATH, '//textarea[contains(@name, "description")]').send_keys("This is description of project")
    driver.find_element(By.XPATH, '//div[contains(@class, "ls-radio-group__button")][1]').click()
    driver.find_element(By.XPATH, '//button[contains(@type, "submit")]').click()
    driver.close()



