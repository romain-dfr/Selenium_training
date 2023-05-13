from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json

def jetX():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.smartsoftgaming.com/GameDemo/JetX")

    driver.switch_to.frame("game-frame")
    elements = driver.find_elements(By.XPATH, "//div[@class='history']//div")

    last100Spins = []
    i = 1
    for spin in elements:
        last100Spins.append({"index": i,"spin": spin.text})
        i += 1

    filePathNameWExt = './' + "last100Spins" + '.json'
    with open(filePathNameWExt, 'w', encoding='utf-8') as fp:
        json.dump(last100Spins, fp, indent=4)

    driver.quit()

def main():
    jetX()


if __name__ == '__main__':
    main()