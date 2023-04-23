import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Utils.driver_connect import get_connection
from selenium.webdriver.support import expected_conditions as EC
def test_render_organization():
    driver = get_connection()

    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    # Press logo
    img_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "ls-menu-header__trigger")]/img')))
    img_element.click()

    # Press organization
    driver.implicitly_wait(15)
    li_organization = driver.find_element(By.XPATH,'//ul/li[2]')
    li_organization.click()

    # Press people ls-email
    ls_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ls-email')))
    ls_email.click()
    driver.close()
