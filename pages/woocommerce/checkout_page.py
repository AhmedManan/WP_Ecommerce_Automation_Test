from playwright.sync_api import Page, expect
import re
from conftest import base_url

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/checkout/'

        # Locators
        self.email_textfield = page.get_by_role("textbox", name="Email address")
        self.first_name_textfield = page.get_by_role("textbox", name="First name")
        self.last_name_textfield = page.get_by_role("textbox", name="Last name")
        self.address_textfield = page.get_by_role("textbox", name="Address", exact=True)
        self.city_name_textfield = page.get_by_role("textbox", name="City")
        self.district_name_dropdown = page.get_by_label("District")
        self.state_name_dropdown = page.get_by_label("State")
        self.postal_code_textfield = page.get_by_role("textbox", name="Postal code (optional)")
        self.phone_number_textfield_locator = page.locator('#shipping-phone')
        self.add_a_note_checkbox = page.get_by_role("checkbox", name="Add a note")
        self.notes_about_your_order_textfield_locator = page.locator(".wc-block-checkout__add-note textarea")
        self.place_order_button = page.get_by_role("button", name="Place Order")
        self.total_price_amount_css_locator = page.locator('.wc-block-components-totals-footer-item-tax-value')

        # User Locators
        self.user_email = 'test@gmail.com'
        self.user_first_name = 'Manan'
        self.user_last_name = 'SQA'
        self.user_address = 'Bashundhara R/A'
        self.user_city = 'Dhaka'
        self.user_district_option = "BD-12"
        self.user_posta_code = '8082'
        self.user_phone_number = '555-555-5555'
        self.user_note = "Please Be careful while Packing"
        self.order_total_price_locator = self.order_total_price_locator = page.get_by_role("row", name="Total")

    def goto(self):
        self.page.goto(base_url+self.page_url)

    def contact_shipping_form(self):
        self.email_textfield.fill(self.user_email)
        self.first_name_textfield.fill(self.user_first_name)
        self.last_name_textfield.fill(self.user_last_name)
        self.address_textfield.fill(self.user_address)
        self.city_name_textfield.fill(self.user_city)
        self.district_name_dropdown.select_option(self.user_district_option)
        self.postal_code_textfield.fill(self.user_posta_code)
        self.phone_number_textfield_locator.fill(self.user_phone_number)
        self.add_a_note_checkbox.check()
        self.notes_about_your_order_textfield_locator.click()
        self.notes_about_your_order_textfield_locator.fill(self.user_note)

    def place_order(self):
        self.place_order_button.click()


