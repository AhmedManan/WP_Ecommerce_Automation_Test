from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page):
        self.page = page

    def open_login(self, url):
        self.page.goto(url+'/wp-admin')

    def enter_username(self, username):
        self.page.fill('#user_login', username)

    def enter_password(self, password):
        self.page.fill('#user_pass', password)

    def click_login(self):
        self.page.click('#wp-submit')

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
