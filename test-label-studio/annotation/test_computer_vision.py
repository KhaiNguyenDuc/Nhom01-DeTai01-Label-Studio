import time

import pytest
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.driver_connect import get_connection
from import_data.test_import_data import test_import__upload_files

# def create_computer_vision_project(driver):
#
#     # Login
#     driver.get("http://127.0.0.1:8080/user/login/")
#     driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
#     driver.find_element(By.NAME, "password").send_keys("k989898k")
#     loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
#     loginBtn.click()
#     # End Login
#
#     # Press create project button
#     driver.get("http://127.0.0.1:8080/projects/")
#     driver.implicitly_wait(15)
#     createProjectBtn = driver.find_element(By.CLASS_NAME, 'ls-button')
#     createProjectBtn.click()
#
#     # Enter value
#     driver.find_element(By.NAME, "name").send_keys("test computer vision project")
#     driver.find_element(By.NAME, "description").send_keys("test description")
#     driver.implicitly_wait(15)
#     saveProjectBtn = driver.find_element(By.XPATH, "//button[contains(@class, 'ls-button') and text()='Delete']")
#     saveProjectBtn.click()
#     driver.close()

def open_annotation_interface(driver):
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # open project

    project = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ls-project-card')]"))
    )
    project.click()



    # open annotation interface
    # Wait until the label button is present and clickable
    task = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dm-table__row-wrapper")][1]'))
    )

    # Click the label button
    task.click()

def open_label_all_task_interface(driver):
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

    # open annotation interface
    # Wait until the label button is present and clickable
    task = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_look_primary")][1]'))
    )

    # Click the label button
    task.click()

def test_submit_annotation():
    driver = get_connection()
    open_annotation_interface(driver)

    # annotate
    label = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(@class,"lsf-label__text") and text()="Airplane"]'))
    )
    label.click()

    # Press submit
    try:
        submit_btn = driver.find_element(By.XPATH, '//button[contains(@class, "lsf-button_look_primary") and text()="Submit"]')
        submit_btn.click()
    except NoSuchElementException:
        test_update_annotation()

    driver.close()

def test_update_annotation():
    driver = get_connection()
    open_annotation_interface(driver)

    # annotate
    label = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(@class,"lsf-label__text") and text()="Airplane"]'))
    )
    label.click()

    # Press Update
    submit_btn = driver.find_element(By.XPATH,
                                     '//button[contains(@class, "lsf-button_look_primary") and text()="Update"]')
    submit_btn.click()

    driver.close()

def test_delete_annotation():

    driver = get_connection()
    open_annotation_interface(driver)

    # Press delete button
    delete_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Delete")]'))
    )
    delete_btn.click()

    # Press confirm delete button
    process_btn = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"lsf-button_look_destructive")]'))
    )
    process_btn.click()

    driver.close()

def test_annotate_all_task():
    driver = get_connection()
    open_label_all_task_interface(driver)

    try:

        while WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(@class,"lsf-label_clickable")][1]'))
        ):
            main_section = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"lsf-main-view__annotation")]'))
            )
            main_section.click()

            # Create an ActionChains object
            actions = ActionChains(driver)

            # Press the "down arrow" key
            actions.send_keys(Keys.DOWN).perform()
            actions.send_keys(Keys.DOWN).perform()

            time.sleep(1)
            # Press labeling
            label = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[contains(@class,"lsf-label_clickable")][1]'))
            )
            label.click()

            # Press submit
            submit_btn = driver.find_element(By.XPATH,
                                             '//button[contains(@class, "lsf-button_look_primary") and text()="Submit"]')
            submit_btn.click()


    except TimeoutException:
        result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"ant-result-title") and text()="No More Tasks Left in Queue"]'))
        )
        assert result.text == "No More Tasks Left in Queue"

    driver.close()

def test_skip_task():

    test_import__upload_files()
    driver = get_connection()
    open_label_all_task_interface(driver)

    # Press skip button
    skip_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "skip-task")]'))
    )
    skip_btn.click()

    backward = driver.find_element(By.XPATH, '//ul[contains(@class, "ls-breadcrumbs__list")]/li[2]')
    backward.click()
    driver.close()
