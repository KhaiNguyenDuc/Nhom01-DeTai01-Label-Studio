import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utils.driver_connect import get_connection


def open_storage_interface(driver):
    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press create project button
    driver.implicitly_wait(15)
    first_button = driver.find_element(By.XPATH, "//button[contains(@class, 'ls-button_withIcon')]")
    first_button.click()

    # Press setting
    driver.implicitly_wait(15)
    settings_link = driver.find_element(By.XPATH, '//a[contains(@class, "ls-main-menu__item") and text()="Settings"]')
    settings_link.click()

    # Press instruction
    driver.implicitly_wait(15)
    instruction_interface = driver.find_element(By.XPATH,
                                       '//a[contains(@class, "ls-main-menu__item") and text()="Cloud Storage"]')
    instruction_interface.click()

def test_add_target_local():
    driver = get_connection()
    open_storage_interface(driver)
    time.sleep(1)

   # Add source storage
    source_btn = driver.find_element(By.XPATH,'//button[contains(@class,"ls-button ls-button_look_") and text()="Add Target Storage"]')
    source_btn.click()


    # Press selected
    select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME,"storage_type"))
    )
    select.click()

    # Select local storage
    local_storage = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//select/option[contains(@value, "localfiles")]'))
    )

    local_storage.click()

    # Enter value
    driver.find_element(By.NAME, "title").send_keys("Test local storage")
    driver.find_element(By.NAME, "path").send_keys("test path")

    # Press add storage
    add_btn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_primary") and text()="Add Storage"]')
    add_btn.click()

def test_delete_target_local():
    driver = get_connection()
    open_storage_interface(driver)

    # Press setting icon
    try:
        setting_icon = driver.find_element(By.XPATH, '//div[contains(@class,"ls-card__header-extra")]/button[contains(@class,"ls-button_withIcon")]')
        setting_icon.click()
    except NoSuchElementException:
        test_add_target_local()
        driver.refresh()
        setting_icon = driver.find_element(By.XPATH,
                                           '//div[contains(@class,"ls-card__header-extra")]/button[contains(@class,"ls-button_withIcon")]')
        setting_icon.click()

    # Press delete span
    delete_span = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,  '//span[contains(@class, "ls-main-menu__item") and text()="Delete"]'))
    )
    delete_span.click()

    # Press button confirm
    confirm_btn = driver.find_element(By.XPATH, '//button[contains(@class, "ls-button_look_destructive") and text()="OK"]')
    confirm_btn.click()

