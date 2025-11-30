from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard
from pages.shortcode_functionality_test_page import ShortcodeFunctionalityTestPage

class TestTableDelete:

    def test_table_delete(self, page: Page):
        # ------------------------------------
        """Update 'Rows Per Page & Table Height'"""
        # ------------------------------------
        login = LoginPage(page)
        login.login()

        flextable_dashboard = FlextableDashboard(page)
        flextable_dashboard.goto()
        flextable_dashboard.delete_table()

        shortcode_page = ShortcodeFunctionalityTestPage(page)
        shortcode_page.goto()
        shortcode_page.check_table_deleted()