import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.driver_connect import get_connection

def open_project_export(driver):
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # open project
    project = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'ls-project-card__title-text') and text()='test project']"))
    )
    project.click()

    # Wait until the import button is present and clickable
    export__btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Export"]'))
    )

    # Click the import button
    export__btn.click()

def export_data(driver,expect_type,export_type):
    time.sleep(1)
    # Get download folder and test file
    EXPECTED_FILE_EXTENSION = expect_type
    user_home = os.path.expanduser("~")
    DOWNLOAD_DIR = os.path.join(user_home, "Downloads")

    open_project_export(driver)

    # Choose export type:
    if export_type != '"JSON"':
        export_div = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"ls-formats__name") and text()='+export_type+']'))
        )
        export_div.click()

    #Press export button
    export_btn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_primary") and text()="Export"]')
    export_btn.click()

    time.sleep(3)

    # Check the file extension
    files = os.listdir(DOWNLOAD_DIR)
    sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(DOWNLOAD_DIR, x)), reverse=True)
    downloaded_file = sorted_files[0]
    _, file_extension = os.path.splitext(downloaded_file)
    assert file_extension == EXPECTED_FILE_EXTENSION, f"File extension {file_extension} does not match {EXPECTED_FILE_EXTENSION}"

def test_export_json():
    driver = get_connection()
    export_data(driver,'.json','"JSON"')
    driver.close()

def test_export_json_min():
    driver = get_connection()
    export_data(driver, '.json', '"JSON-MIN"')
    driver.close()

def test_export_csv():
    driver = get_connection()
    export_data(driver, '.csv', '"CSV"')
    driver.close()

def test_export_tsv():
    driver = get_connection()
    export_data(driver, '.csv', '"TSV"')
    driver.close()

def test_export_coco():
    driver = get_connection()
    export_data(driver, '.zip', '"COCO"')
    driver.close()
