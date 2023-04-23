import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    project = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ls-project-card__title-text') and text()='test data project']"))
    )
    project.click()

    # Press setting
    driver.implicitly_wait(15)
    settings_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "ls-button_size_compact") and text()="Settings"]'))
    )
    # Click the setting link
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
    driver.find_element(By.NAME, "name").send_keys("test create project")
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

    driver.find_element(By.XPATH, '//textarea[contains(@name, "description")]').send_keys("This is description of project")
    driver.find_element(By.XPATH, '//div[contains(@class, "ls-radio-group__button")][1]').click()
    driver.find_element(By.XPATH, '//button[contains(@type, "submit")]').click()
    driver.close()

def test_delete_exist_project():
    driver = get_connection()
    open_general_setting(driver)

    # Press Danger Zone
    driver.implicitly_wait(15)
    lb_interface = driver.find_element(By.XPATH,
                                       '//a[contains(@class, "ls-main-menu__item") and text()="Danger Zone"]')
    lb_interface.click()

    #Press delete project
    delete_btn = driver.find_element(By.XPATH,'//button[contains(@class,"ls-button_look_danger") and text()="Delete Project"]')
    delete_btn.click()

    # Press proceed
    driver.implicitly_wait(15)
    proceed_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_destructive") and text()="Proceed"]')
    proceed_btn.click()
    driver.close()

def test_drop_tabs_exist_project():
    driver = get_connection()

    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press project button
    project = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'ls-project-card__title-text') and text()='computer vision project']"))
    )
    project.click()

    # Press setting
    driver.implicitly_wait(15)
    settings_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "ls-button_size_compact") and text()="Settings"]'))
    )
    # Click the setting link
    settings_link.click()

    # Press Danger Zone
    driver.implicitly_wait(15)
    lb_interface = driver.find_element(By.XPATH,
                                       '//a[contains(@class, "ls-main-menu__item") and text()="Danger Zone"]')
    lb_interface.click()

    # Press delete project
    delete_btn = driver.find_element(By.XPATH,
                                     '//button[contains(@class,"ls-button_look_danger") and text()="Drop All Tabs"]')
    delete_btn.click()

    # Press proceed
    driver.implicitly_wait(15)
    proceed_btn = driver.find_element(By.XPATH,
                                      '//button[contains(@class,"ls-button_look_destructive") and text()="Proceed"]')
    proceed_btn.click()
    driver.close()