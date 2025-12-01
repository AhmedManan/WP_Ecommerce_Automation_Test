from playwright.sync_api import Page, expect
import re
from conftest import base_url

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/wp-admin/admin.php?page=wc-orders'

        # Locators

        # User Locators

    def goto(self):
        self.page.goto(base_url+self.page_url)

    def confirm_order(self):
        return


