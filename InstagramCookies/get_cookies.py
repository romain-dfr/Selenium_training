import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
load_dotenv()
import os

USER = os.environ.get('INSTA_USERNAME')
PASSWORD = os.getenv('INSTA_PASSWORD')

def save_cookies_file(url, file_name):
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys(USER)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//button[@class="_acan _acap _acas _aj1-"]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='_acan _acap _acas _aj1-']"))).click()
    
    pickle.dump(driver.get_cookies(), open(file_name, "wb"))
    driver.quit()

save_cookies_file('https://www.instagram.com/', './perso/ex4/instagram_cookies.pkl')
