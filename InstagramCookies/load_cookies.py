import pickle
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_cookies_file(url, file_name):
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    cookies = pickle.load(open(file_name, "rb"))
    print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='_a9-- _a9_1']"))).click()

    sleep(1000)

load_cookies_file('https://www.instagram.com/', './perso/ex4/instagram_cookies.pkl')
