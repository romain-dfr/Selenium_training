from selenium import webdriver
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
    driver.get("https://amazon.com")
    wait = WebDriverWait(driver, 10)
    # create WebElement for a search box
    search_box = driver.find_element(By.ID, 'twotabsearchtextbox') #twotabsearchtextbox  nav-bb-search
    # type the keyword in searchbox
    search_box.send_keys("iphone")
    driver.find_element(By.ID, 'nav-search-submit-button').click()

    product = {}
    products = [product]

    #next page
    while True:
        try:
            next_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')))
            
            items = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
            
            for item in items:
                # find price
                whole_price = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]') # find_elements returns a list so if it's empty it will be just []
                fraction_price = item.find_elements(By.XPATH, './/span[@class="a-price-fraction"]')
                
                if whole_price != [] and fraction_price != []:
                    price = '.'.join([whole_price[0].text, fraction_price[0].text])
                    print(price+'\n')
                else:
                    price = 0
                product['price'] = price
                
                # find link
                link = item.find_element(By.XPATH, './/a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').get_attribute("href")
                product['link'] = link

                products.append(product)
                product = {}

            next_page.click()
        except:
            driver.quit()
            print(products)
            filePathNameWExt = './' + "amazonIphone" + '.json'
            with open(filePathNameWExt, 'w') as fp:
                json.dump(products, fp, indent=4)

def main():
    amazon()


if __name__ == '__main__':
    main()