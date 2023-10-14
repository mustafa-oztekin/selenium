from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "http://github.com"

driver.get(url)

searchInput = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button").click()
time.sleep(1)
searchInput = driver.find_element(By.XPATH, "//*[@id='query-builder-test']")
time.sleep(1)
searchInput.send_keys('python')
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(4)

#result = driver.page_source


result = driver.find_elements(By.CSS_SELECTOR, ".Box-sc-g0xbh4-0 h3 a")
time.sleep(1)
for element in result:
    print(element.text)
driver.close()
