from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from Utils.driver_connect import get_connection


def open_instruction_interface(driver):
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
                                       '//a[contains(@class, "ls-main-menu__item") and text()="Instructions"]')
    instruction_interface.click()

def test_add_instruction():
    driver = get_connection()
    open_instruction_interface(driver)
    driver.find_element(By.NAME,"expert_instruction").send_keys("Test instruction")
    save_btn = driver.find_element(By.XPATH, '//button[contains(@type,"submit")]')
    save_btn.click()