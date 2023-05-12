from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def amazon():
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.amazon.fr/s?i=toys&bbn=322088011&rh=n%3A322086011%2Cn%3A363575031%2Cp_n_age_range%3A304554031%7C407102031%2Cp_6%3AA1X6FK5RDHNB96&dc&page=2&qid=1678717580&rnid=322088011&ref=sr_pg_2")
    wait = WebDriverWait(driver, 10)

    product = {}
    products = [product]
    
    items = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
    
    for item in items:
        product = {}
        #find title
        title = item.find_element(By.XPATH, './/span[@class="a-size-base-plus a-color-base a-text-normal"]').text
        product['title'] = title

        # find price
        whole_price = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]') # find_elements returns a list so if it's empty it will be just []
        fraction_price = item.find_elements(By.XPATH, './/span[@class="a-price-fraction"]')
        
        if whole_price != [] and fraction_price != []:
            price = '.'.join([whole_price[0].text, fraction_price[0].text])
        if whole_price != [] and fraction_price == []:
            price = whole_price[0].text
        else:
            price = 0
        product['price'] = price

        # find age
        try:
            age = item.find_element(By.XPATH, ".//div[@class='a-section a-spacing-small puis-padding-left-small puis-padding-right-small']//div[@class='a-section a-spacing-none a-spacing-top-mini']//div[@class='a-row a-size-base a-color-base']//span")
            product['age'] = age.text
        except:
            product['age'] = "None"
        
        products.append(product)

    driver.quit()
    filePathNameWExt = './' + "amazonToys" + '.json'
    with open(filePathNameWExt, 'w', encoding='utf-8') as fp:
        json.dump(products, fp, indent=4)

def main():
    amazon()


if __name__ == '__main__':
    main()