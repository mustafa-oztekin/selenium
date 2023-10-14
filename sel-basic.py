from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
#driver.save_screenshot("oyet_homepage.png")
url = "https://github.com/mustafa-oztekin"
driver.get(url)
if "mustafa-oztekin" in driver.title:
    print(driver.title)

# driver.back()
# driver.forwad()

time.sleep(2)
driver.close()