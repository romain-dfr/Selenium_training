from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import sys
from Metro import metro
import signal

def signal_handler(sig, frame):
    print("\nYou pressed Ctrl+C, Ctrl+Z or Ctrl+D. Exiting gracefully.")
    sys.exit(0)

def main():
    # driver = setup("https://shop.metro.fr/") // using cookies
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(f"--user-data-dir=/home/romain/.config/google-chrome/Default1")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    signal.signal(signal.SIGINT, signal_handler)
    try: 
        print(sys.argv[1])
        metro(driver, sys.argv[1])

    except:
        print("No argument passed")


if __name__ == '__main__':
    main()