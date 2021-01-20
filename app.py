from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FacebookBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.facebook.com/")
        time.sleep(4)
        email = bot.find_element_by_name('email')
        password = bot.find_element_by_name('pass')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)


mycred = FacebookBot('', '')  # enter your mail and password
mycred.login()
