from playwright.sync_api import Page

from pages.woocommerce.order_history_page import OrderHistoryPage
from pages.woocommerce.product_page import ProductPage
from pages.woocommerce.checkout_page import CheckoutPage
from pages.woocommerce.cart_page import CartPage
# Ensure you import get_csv_data from wherever it is defined
from utils.product_data_utils import get_csv_data
from playwright.sync_api import Page, expect


class TestCheckoutFlow:

    expected_total_sum = 3461.85

    # 1. REMOVE @pytest.mark.parametrize
    # The test will now run exactly once.
    def test_check_out_flow(self, page: Page):
        # ------------------------------------
        """End-to-End Checkout Flow"""
        # ------------------------------------

        products_to_add = get_csv_data()

        for product in products_to_add:
            page_url_slug = product["page_url_slug"]

            print(f"Adding product: {page_url_slug} to cart...")

            product_page = ProductPage(page, page_url_slug)

            product_page.goto(page_url_slug)

            product_page.add_to_cart_button.click()


        cart_page = CartPage(page)
        cart_page.goto()
        cart_page.proceed_to_checkout()

        checkout_page = CheckoutPage(page)
        # checkout_page.goto()
        checkout_page.contact_shipping_form()
        checkout_page.place_order()

        order_history = OrderHistoryPage(page)
        order_history.goto()
        page.pause()