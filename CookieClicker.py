from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_cookies():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    wait = WebDriverWait(driver, 10)
    langue = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-FR")))
    langue.click()
    try:
        cookie = wait.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
        cookie.click()
    except:
        pass
    storeBulk100 = wait.until(EC.element_to_be_clickable((By.ID, "storeBulk100")))
    storeBulk100.click()
    while (1):
        driver.find_element(By.ID, "bigCookie").click()
        product = driver.find_elements(By.XPATH, "//*[@class ='product unlocked enabled']")
        craft = driver.find_elements(By.XPATH, "//*[@class ='crate upgrade enabled']")
        try: 
            product[-1].click()
        except:
            pass
        try:
            craft[-1].click()
        except:
            pass
    sleep(1000)

def main():
    click_cookies()


if __name__ == '__main__':
    main()