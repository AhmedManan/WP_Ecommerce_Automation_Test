from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.woocommerce.order_history_page import OrderHistoryPage
from utils.product_data_utils import get_csv_data, get_expected_product_names
from playwright.sync_api import Page, expect


class TestUserAccountOrderHistory:

    def test_check_out_flow(self, page: Page):
        # ------------------------------------
        """User Account Order History"""
        # ------------------------------------

        csv_data_list_of_dicts = get_csv_data()

        login_page = LoginPage(page)
        login_page.login()

        order_history = OrderHistoryPage(page)
        order_history.goto()
        order_history.view_order_details()

        product_names_list = order_history.get_all_products_in_order()

        expected_product_names_list = get_expected_product_names(csv_data_list_of_dicts)

        actual_set = set(product_names_list)
        expected_set = set(expected_product_names_list)

        assert expected_set == actual_set, \
            f"Product lists do not match. Expected: {expected_set}, Actual: {actual_set}"

