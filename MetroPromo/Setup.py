import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from dotenv import load_dotenv
load_dotenv()
import os

USER = os.environ.get('METRO_USERNAME')
PASSWORD = os.getenv('METRO_PASSWORD')

def save_cookies_file(driver, url, file_name):
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='content-container']")))
    driver.execute_script('''return document.querySelector('cms-cookie-disclaimer').shadowRoot.querySelector('button[class="accept-btn btn-primary field-accept-button-name"]')''').click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='sd-geolocation-cancel-button btn btn-link']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn-primary btn btn-default']"))).click()

    wait.until(EC.visibility_of_element_located((By.NAME, "user_id"))).send_keys(USER)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, 'submit').click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='content-container']")))
    pickle.dump(driver.get_cookies(), open(file_name, "wb"))
    driver.quit()


def load_cookies_file(driver, url, file_name):
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    cookies = pickle.load(open(file_name, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='sd-geolocation-cancel-button btn btn-link']"))).click()

    return driver


def setup_chromedriver():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    return webdriver.Chrome(service=service, options=chrome_options)

def setup(url):
    driver = setup_chromedriver()
    try:
        driver = load_cookies_file(driver, url, "./metro_cookies.pkl")
    except:
        save_cookies_file(driver, url, "./metro_cookies.pkl")
        driver = setup_chromedriver()
        driver = load_cookies_file(driver, url, "./metro_cookies.pkl")
    
    return driver