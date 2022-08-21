import os, sys
from random import choice, randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


class InstagramBot():
    def __init__(self):
        os.chdir(sys.path[0])
        
        # browser settings
        options = Options()
        self.browser = webdriver.Firefox(options=options)
        self.browser.maximize_window()
        self.browser.implicitly_wait(7)


    def login(self, username:str, password:str) -> None:

        # got to url
        self.browser.get('https://www.instagram.com/')
        sleep(2)

        # get inputs and send username, password
        username_input = self.browser.find_element(by=By.CSS_SELECTOR, value="input[name='username']",)
        password_input = self.browser.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
        username_input.send_keys(username)
        sleep(randint(2, 5))
        password_input.send_keys(password)

        # click on login button
        login_button = self.browser.find_element(by=By.XPATH, value="//button[@type='submit']")
        sleep(randint(2, 5))
        login_button.click()

        sleep(randint(2, 5))

        self.browser.find_element(by=By.XPATH, value="//button[text()='Not Now']").click()
        sleep(randint(2, 5))
        self.browser.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]").click()
        sleep(randint(2, 5))


    def follow(self, username:str) -> None:
        try:
            # go to user profile
            self.browser.get(f"https://www.instagram.com/{username}")
            sleep(randint(10, 30))

            # click on follow bottun
            self.browser.find_element(by=By.XPATH, value="//div[text()='Follow']").click()
            sleep(randint(2, 5))

        except: pass


    def unfollow(self, username:str):
        try:
            # go to user profile
            self.browser.get(f"https://www.instagram.com/{username}")
            sleep(randint(10, 30))

            # click on unfollow bottun
            self.browser.find_element(by=By.CSS_SELECTOR, value="._abb3 > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)").click()
            sleep(2)
            self.browser.find_element(by=By.CSS_SELECTOR, value="button._a9--:nth-child(1)").click()

        except: pass


    def like_post(self, id_:str) -> None:
        try:
            # go to post url
            self.browser.get(f"https://www.instagram.com/p/{id_}")
            sleep(randint(10, 60))

            # click on like button
            self.browser.find_element(by=By.CSS_SELECTOR, value="._aamw > button:nth-child(1)").click()
            sleep(choice([5, 10, 15, 20]))

        except: pass


    def unlike_post(self, id_:str) -> None:
        try:
            # go to post url
            self.browser.get(f"https://www.instagram.com/p/{id_}")
            sleep(randint(10, 60))

            # click on unlike button
            self.browser.find_element(by=By.CSS_SELECTOR, value="._aamw > button:nth-child(1)").click()
            sleep(choice([5, 10, 15, 20]))

        except: pass


    def comment(self, id_:str, comment:str) -> None:
        try:
            # go to post url
            self.browser.get(f"https://www.instagram.com/p/{id_}")
            sleep(randint(10, 60))

            # send comment to input
            comment_input = self.browser.find_element(by=By.TAG_NAME, value='textarea')
            comment_input.send_keys(comment)
            sleep(randint(2, 5))

            # click on comment button
            self.browser.find_element(by=By.XPATH, value="//div[text()='Post']").click()
            sleep(randint(2, 5))

        except: pass


    def search_tag(self, tag_name:str, count:int) -> list:
        # search tag
        self.browser.get(f"https://www.instagram.com/explore/tags/{tag_name}")

        # get post url
        posts = self.browser.find_elements(by=By.XPATH, value=f"(//a)[position()<{count}]")
        posts_link = [i.get_attribute("href").split("https://www.instagram.com/p/")[1] for i in posts]
        sleep(randint(2, 5))

        return posts_link


    def get_post_writer(self, id_:str) -> str:
        # go to post url
        self.browser.get(f"https://www.instagram.com/p/{id_}")
        sleep(randint(10, 60))

        # get post author
        writer = self.browser.find_element(by=By.CSS_SELECTOR, value="._aaqt > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)").text

        return writer


    def get_user_posts(self, username:str, count:int=5):
        # go to user profile
        self.browser.get(f"https://www.instagram.com/{username}")
        sleep(randint(10, 20))

        # get posts url
        posts = self.browser.find_elements(by=By.XPATH, value=f"(//a)[position()<{count}]")
        posts_link = []
        try:
            posts_link = [i.get_attribute("href").split("https://www.instagram.com/p/")[1]  for i in posts if "https://www.instagram.com/p/" in i.get_attribute("href")]
        except: pass

        return posts_link


    def end(self):
        self.browser.close()


bot = InstagramBot()
sample_comments = ["greate!", "Thanks", "👌👌", "Well🙏", "😍😍"]

bot.login("s_ali_mi1386", 'ali0250902109')
posts = bot.search_tag("python", 5)
for post in posts:
    bot.like_post(post)
    bot.comment(post, comment=choice(sample_comments))
    author = bot.get_post_writer(post)
    for p in bot.get_user_posts(author, 2):
        bot.like_post(p)
        bot.comment(p, comment=choice(sample_comments))
    bot.follow(author)

bot.end()
