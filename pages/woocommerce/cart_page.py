from playwright.sync_api import Page, expect
from conftest import base_url

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/cart'

        # Locators
        self.proceed_to_checkout_button = page.get_by_role("link", name="Proceed to Checkout")

    def goto(self):
        self.page.goto(base_url+self.page_url)

    def proceed_to_checkout(self):
        expect(self.proceed_to_checkout_button).to_be_visible()
        self.proceed_to_checkout_button.click()


