from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        wait = WebDriverWait(self.browser, 10)
        username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")))
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")))
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[3]/button")))
        
        #self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
        #self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
        
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button.click()

        #self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()
        #time.sleep(10)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".xnz67gz.x14yjl9h.xudhj91.x18nykt9.xww2gxu.x9f619.x1lliihq.x2lah0s.x6ikm8r.x10wlt62.x1n2onr6.x1ykvv32.xougopr.x159fomc.xnp5s1o.x194ut8o.x1vzenxt.xd7ygy7.xt298gk.x1xrz1ek.x1s928wv.x1n449xj.x2q1x1w.x1j6awrg.x162n7g1.x1m1drc7")))

    def getFollowers(self):
        wait = WebDriverWait(self.browser, 10)
        self.browser.get(f"https://www.instagram.com/{self.username}")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd"))).click()

        #self.browser.find_element(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd").click()
        #time.sleep(3)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role=dialog]")))
        dialog = self.browser.find_element(By.CSS_SELECTOR, "._aano")

        #dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role=dialog]").find_element(By.CSS_SELECTOR, "._aano")
        followersCount = len(dialog.find_elements(By.CSS_SELECTOR, ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
        
        print(f"first count: {followersCount}")

        action = webdriver.ActionChains(self.browser)
        dialog.click()
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(.1)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(.1)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(1)

        while True:
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(.1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(.1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements(By.CSS_SELECTOR, ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
            if followersCount != newCount:
                followersCount = newCount
                print(f"new count: {newCount}")
                time.sleep(1)
            else:
                break
        followers = dialog.find_elements(By.CSS_SELECTOR, ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        
        for user in followers:
            #link = user.find_element(By.CSS_SELECTOR, "span").text
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            print(link)

    def saveFollowers(self, max):
        wait = WebDriverWait(self.browser, 10)
        self.browser.get(f"https://www.instagram.com/{self.username}")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd"))).click()


        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role=dialog]")))
        dialog = self.browser.find_element(By.CSS_SELECTOR, "._aano")

        followersCount = len(dialog.find_elements(By.CSS_SELECTOR, ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
        
        print(f"first count: {followersCount}")

        action = webdriver.ActionChains(self.browser)
        dialog.click()
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(.1)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(.1)
        action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
        time.sleep(1)

        while followersCount <= max:
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(.1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(.1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements(By.CSS_SELECTOR, ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
            if followersCount != newCount:
                followersCount = newCount
                print(f"new count: {newCount}")
                time.sleep(1)
            else:
                break
        followers = dialog.find_elements(By.CSS_SELECTOR, ".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")

        followerList = []
        i = 0
        for user in followers:
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#            print(link)
            followerList.append(link)
            i += 1
            if i == max:
                break
            print(link)

        with open("followers.txt", "w", encoding="utf-8") as file:
            for item in followerList:
                file.write(item + "\n")

    def followUser(self, username):
        wait = WebDriverWait(self.browser, 10)
        self.browser.get("https://www.instagram.com/" + username)
        followButton = wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        followButton = self.browser.find_element(By.TAG_NAME, "button")
        #print(followButton)

        if followButton.text != "Takiptesin":
            followButton.click()
            time.sleep(5)
        else:
            print("zaten takip ediyorsun...")

    def unFollowUser(self, username):
        wait = WebDriverWait(self.browser, 10)
        self.browser.get("https://www.instagram.com/" + username)
        followButton = wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        followButton = self.browser.find_element(By.TAG_NAME, "button")


        if followButton.text == "Takiptesin":
            followButton.click()
            time.sleep(3)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role=dialog]")))
            dialog = self.browser.find_elements(By.CSS_SELECTOR, ".x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft")
            for button in dialog:
                but = button.find_element(By.CSS_SELECTOR, ".x1lliihq.x193iq5w.x6ikm8r.x10wlt62.xlyipyv.xuxw1ft").text
                print(but)
        else:
            print("zaten takip etmiyorsun...")

insta = Instagram(username, password)
insta.signIn()
insta.saveFollowers(50)
#insta.getFollowers()
#insta.followUser("mustafa.oztekin26")
#insta.unFollowUser("mustafa.oztekin26")



"""
liste = ["mustafa.oztekin26", "", "", "", ""]
for user in liste:
    insta.followUser(user)
    time.sleep(3)
"""