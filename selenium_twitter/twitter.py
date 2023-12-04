from twitterUserInfo import username, password, phonenumber
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Twitter:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.phonenumber = phonenumber

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        wait = WebDriverWait(self.browser, 10)

        username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")))
        username_input.send_keys(self.username)
        username_input.send_keys(Keys.ENTER)

        phonenumber_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")))
        phonenumber_input.send_keys(self.phonenumber)
        phonenumber_input.send_keys(Keys.ENTER)

        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu")))
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(10)

twitter = Twitter(username, password)
twitter.signIn()