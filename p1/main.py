import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="chromedriver.exe")
# Initialize the browser with the service
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-infobars")
# options.add_argument("--start-maximized")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service = service)
driver.get("https://google.com/")
element = driver.find_element(By.CLASS_NAME, "gLFyf")
if element:
    print("Element found")
element.send_keys("Hello World"+Keys.ENTER)

time.sleep(10)

#print(element.text)
driver.quit()

