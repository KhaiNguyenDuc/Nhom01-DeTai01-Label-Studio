import time
import pyautogui
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.driver_connect import get_connection

def open_project_import_form(driver):
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # open project
    project = driver.find_element(By.XPATH, "//div[contains(@class, 'ls-project-card')]")
    project.click()

    # Wait until the import button is present and clickable
    import_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Import"]'))
    )

    # Click the import button
    import_btn.click()

def test_import__dataset_url():

    driver = get_connection()
    open_project_import_form(driver)



    # Upload files
    driver.find_element(By.NAME,"url").send_keys(r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAc7xfOykQmrdNnp3s0CF4MFJLlQGtdZ1H6A&usqp=CAU")
    submit_btn = driver.find_element(By.XPATH, '//button[contains(@type,"submit")]')
    submit_btn.click()

    # Save data
    save_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Import"]')
    save_btn.click()

    driver.close()

@pytest.mark.file_explorer
def test_import__upload_files():

    driver = get_connection()
    open_project_import_form(driver)

    # Upload files
    upload_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-upload_page__upload-button")]')
    upload_btn.click()

    time.sleep(2)
    # Choose file from file explorer
    pyautogui.write(r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\ca_tim.jpg")
    pyautogui.press('enter')

    # Save data
    save_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Import"]')
    save_btn.click()

    driver.close()