import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utils.driver_connect import get_connection


def create_project(driver,name,description,template,order,file):
    time.sleep(1)
    # Press create project button
    driver.get("http://127.0.0.1:8080/projects/")
    driver.implicitly_wait(15)
    createProjectBtn = driver.find_element(By.CLASS_NAME, 'ls-button')
    createProjectBtn.click()


    # Enter computer vision
    driver.implicitly_wait(25)
    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.NAME, "description").send_keys(description)

    # Enter template:
    labeling_setup = driver.find_element(By.XPATH, '//ul[contains(@class,"ls-toggle-items")]/li[3] ')
    labeling_setup.click()

    # Select interface:
    labeling_interface = driver.find_element(By.XPATH, '//ul/li[contains(@class,"ls-templates-list__group")]['+order+']')
    labeling_interface.click()

    # Select template:
    template = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//h3[text()='+template+']'))
    )
    template.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"lsf-main-view__annotation")]'))
    )
    time.sleep(2)
    # Import Data
    labeling_setup = driver.find_element(By.XPATH, '//ul[contains(@class,"ls-toggle-items")]/li[2] ')
    labeling_setup.click()

    # Upload files
    input_upload = driver.find_element(By.ID, 'file-input')
    input_upload.send_keys(file)

    saveProjectBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ls-button') and text()='Save']"))
    )
    saveProjectBtn.click()

    # Back ward
    driver.implicitly_wait(15)
    driver.get("http://localhost:8080/projects")


def test_init_data(driver):

    # Login
    driver.get("http://127.0.0.1:8080/user/login/")
    driver.find_element(By.NAME, "email").send_keys("duckhailinux@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("k989898k")
    loginBtn = driver.find_element(By.CLASS_NAME, 'ls-button_look_primary')
    loginBtn.click()
    # End Login

    create_project(driver, 'test project', 'test description', '"Semantic Segmentation with Polygons"', '1',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\chanh.jpg")
    create_project(driver, 'test data project', 'test description', '"Semantic Segmentation with Polygons"', '1',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\chanh.jpg")
    create_project(driver, 'test label project', 'test description', '"Semantic Segmentation with Polygons"', '1',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\chanh.jpg")

    create_project(driver,'computer vision project', 'test description', '"Semantic Segmentation with Polygons"','1',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\ca_tim.jpg")
    create_project(driver, 'speech process project', 'test description', '"Automatic Speech Recognition"','3',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\test_audio.mp3")
    create_project(driver, 'converational AI project', 'test description', '"Coreference Resolution & Entity Linking"','4',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\tao_do.jpg")
    create_project(driver, 'ranking and scoring project', 'test description', '"Document Retrieval"','5',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\ca_tim.jpg")
    create_project(driver, 'structured Data Parsing project', 'test description', '"PDF Classification"','6',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\ca_tim.jpg")
    create_project(driver, 'video project', 'test description', '"Video Object Tracking"','8',r"K:\HCMUTE\Nam3_Repository\Nhom01-DeTai01-Label-Studio\test-label-studio\uploads\test_video.mp4")

    # Already close

