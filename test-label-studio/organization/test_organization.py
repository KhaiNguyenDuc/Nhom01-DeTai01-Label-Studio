import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Utils.driver_connect import get_connection
from selenium.webdriver.support import expected_conditions as EC

def press_organization(driver):
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press logo
    img_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ls-menu-header__trigger")]/img')))
    img_element.click()

    # Press organization
    driver.implicitly_wait(15)
    li_organization = driver.find_element(By.XPATH, '//ul/li[2]')
    li_organization.click()

def add_people(driver,email):
    press_organization(driver)

    # Press add people button
    addPeople = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Add People"]')))
    addPeople.click()

    # Enter email
    inputEmail = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "email")))
    inputEmail.send_keys(email)

    # Choose Role
    role_admin = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//select/option[2]")))
    role_admin.click()

    # Press add
    btnSubmit = driver.find_element(By.XPATH, "//button[contains(@class,'ls-button_look_') and text()='Add']")
    btnSubmit.click()

    # Quit
    buttonQuit = driver.find_element(By.XPATH,"//button[@class='ls-button ls-button_type_text ls-button_look_ ls-button ls-button_type_text ls-button_look_ ls-button_withIcon ls-modal__close']")
    buttonQuit.click()

def test_render_organization():
    driver = get_connection()
    press_organization(driver)
    # Press people ls-email
    ls_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ls-email')))
    ls_email.click()
    driver.close()

def test_add_people():
    driver = get_connection()
    add_people(driver,"duckhai0606@gmail.com")

def test_invalid_email():
    driver = get_connection()
    press_organization(driver)

    # Press add people button
    addPeople = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Add People"]')))
    addPeople.click()

    # Enter email
    inputEmail = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "email")))
    inputEmail.send_keys("duckhai0606")

    # Choose Role
    role_admin = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//select/option[2]")))
    role_admin.click()

    # Press add
    btnSubmit = driver.find_element(By.XPATH, "//button[contains(@class,'ls-button_look_') and text()='Add']")
    btnSubmit.click()

    error = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[contains(@class,'error')]")))

    assert error.text == "Email format is incorrect!!"

def test_invalid_role():
    driver = get_connection()
    press_organization(driver)

    # Press add people button
    addPeople = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Add People"]')))
    addPeople.click()

    # Enter email
    inputEmail = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "email")))
    inputEmail.send_keys("duckhai0606123@gmail.com")

    # Press add
    btnSubmit = driver.find_element(By.XPATH, "//button[contains(@class,'ls-button_look_') and text()='Add']")
    btnSubmit.click()

    error = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//i[contains(@class,'error')]")))

    assert error.text == "Please choose Role!!"

def test_signup_with_token():
    driver = get_connection()
    email = "duckhai1008@gmail.com"
    add_people(driver,email)

    # Get token
    invite_link = driver.find_element(By.XPATH,"//input[@class='ls-input'][@readonly='']")
    link_value = invite_link.get_attribute("value")

    # Press user profile
    user_profile = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ls-userpic")]')))
    user_profile.click()

    # Press logout
    logout_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[contains(@class, "ls-main-menu")]/li[2]')))
    logout_btn.click()

    # Sigup with new user
    driver.get(link_value)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    signupBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    signupBtn.click()

    # Check organization
    # Press logo
    img_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ls-menu-header__trigger")]/img')))
    img_element.click()

    # Press organization
    driver.implicitly_wait(15)
    li_organization = driver.find_element(By.XPATH, '//ul/li[2]')
    li_organization.click()
