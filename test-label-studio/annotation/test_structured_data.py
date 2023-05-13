
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.driver_connect import get_connection



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
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'ls-projects-page__link')][2]"))
    )
    project.click()





    # open annotation interface
    # Wait until the label button is present and clickable
    task = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "dm-table__row-wrapper")][1]'))
    )

    # Click the label button
    task.click()

def test_submit_annotation():
    driver = get_connection()
    open_annotation_interface(driver)

    # annotate
    rating = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[contains(@class,"ant-rate")]/li[2]'))
    )
    rating.click()
    
    choice_leaf = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"lsf-choice_leaf")][1]'))
    )
    choice_leaf.click()

    # Press submit
    try:
        submit_btn = driver.find_element(By.XPATH, '//button[contains(@class, "lsf-button_look_primary") and text()="Submit"]')
        submit_btn.click()
    except NoSuchElementException:
        update_annotation(driver)

    driver.close()

def update_annotation(driver):

    # Press Update
    submit_btn = driver.find_element(By.XPATH,
                                     '//button[contains(@class, "lsf-button_look_primary") and text()="Update"]')
    submit_btn.click()

