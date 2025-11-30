from playwright.sync_api import Page, expect
from conftest import base_url

class ProductPage:

    def __init__(self, page: Page, base_url: str):
        self.page = page
        # self.base_url = base_url
        self.page_url = '/'

        # Locators
        self.add_to_cart_button = page.get_by_text("Add to cart", exact=True)
        self.close_add_to_cart_sidebar = page.locator("#close-cart-sidebar-btn")
        self.view_cart_link = page.get_by_role("link", name="View cart")

    def goto(self, page_url_slug: str):
        self.page.goto(base_url + page_url_slug)

    def add_product_to_cart(self):
        expect(self.add_to_cart_button).to_be_visible()
        self.add_to_cart_button.click()
        # self.close_add_to_cart_sidebar.click()

    def view_cart(self):
        expect(self.view_cart_link).to_be_visible()
        self.view_cart_link.click()



