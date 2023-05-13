from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fastfingers():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://10fastfingers.com/typing-test")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyButtonDecline"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "row1")))
    input = wait.until(EC.visibility_of_element_located((By.ID, "inputfield")))
    while True:
        try:
            word = driver.find_elements(By.XPATH, "//span[@class ='highlight']")
            input.send_keys(word[0].text + " ")
        except:
            break

    driver.quit()
    
def main():
    fastfingers()


if __name__ == '__main__':
    main()