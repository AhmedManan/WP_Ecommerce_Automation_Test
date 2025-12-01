from playwright.sync_api import Page, expect
import re
from conftest import base_url

class OrderHistoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/my-account/orders'

        # Locators
        self.view_order_details_button = page.get_by_role("cell", name="View order")
        self.product_name_locator = page.locator('.product-name')
        # self.product_name_locator = page.locator('xpath=table/tbody/tr/td/a')


    def goto(self):
        self.page.goto(base_url+self.page_url)

    def view_order_details(self):
        self.view_order_details_button.click()

    def get_all_products_in_order(self):

        all_names_with_whitespace = self.product_name_locator.all_text_contents()

        product_names_list = []

        for name in all_names_with_whitespace:

            # Cleaning the name, replacing the unwanted value with ''
            cleaned_name = name.replace('×\xa01', '').strip()

            # Converting the webpage's curly apostrophe (’) to the CSV's straight apostrophe (') to prevent data mismatch
            cleaned_name = cleaned_name.replace('’', "'")

            # Filter out unwanted strings, 'Product'
            if cleaned_name and cleaned_name != 'Product':
                product_names_list.append(cleaned_name)

        print("\nFound Product Names: ")
        print(product_names_list)

        return product_names_list


