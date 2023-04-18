import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from Utils.driver_connect import get_connection

def test_create_webhook():
    driver = get_connection()

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

    # Press webhook
    webhook = driver.find_element(By.XPATH,
                                       '//a[contains(@class, "ls-main-menu__item") and text()="Webhooks"]')
    webhook.click()

    #Press add webhooks button
    driver.implicitly_wait(15)
    addWebhookBtn = driver.find_element(By.XPATH, '//button[contains(@class,"ls-button_look_") and text()="Add Webhook"]')
    addWebhookBtn.click()
