from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard
from pages.shortcode_functionality_test_page import ShortcodeFunctionalityTestPage

class TestTableCustomization:

    def test_table_entry_info_pagination(self, page: Page):
        # ------------------------------------
        """Enable Entry Info & Pagination"""
        # ------------------------------------
        login = LoginPage(page)
        login.login()

        flextable_dashboard = FlextableDashboard(page)
        flextable_dashboard.goto()
        flextable_dashboard.navigate_to_table_customization_entry_level_pagination()

        shortcode_page = ShortcodeFunctionalityTestPage(page)
        shortcode_page.goto()
        shortcode_page.check_entry_level_exist()
        shortcode_page.check_pagination_exist()