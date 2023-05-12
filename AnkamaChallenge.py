from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def ankama():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://support.ankama.com/hc/fr/requests/new?ticket_form_id=360001732753")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Et plus précisément…']//following-sibling::a[@class='nesty-input']"))).click()
    
    action = ActionChains(driver)
    action.send_keys(Keys.DOWN)
    action.send_keys(Keys.ENTER)
    action.perform()
    sleep(1000)
    driver.quit()

def main():
    ankama()


if __name__ == '__main__':
    main()