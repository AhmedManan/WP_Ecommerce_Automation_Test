from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard

class TestFlextableDashboard:


    def test_navigate_to_flextable_dashboard(self, page: Page):
        # ------------------------------------
        """Navigate to FlexTable Dashboard"""
        # ------------------------------------

        # First Perform Login
        login = LoginPage(page)
        login.login()


        # Navigate to Flextable page
        flextable_dashboard = FlextableDashboard(page)
        flextable_dashboard.page_fully_loaded()

        flextable_dashboard.is_dashboard_visible()
        flextable_dashboard.is_dashboard_visible()

    def test_create_a_new_table_using_google_sheet_input(self, page: Page):
        # ------------------------------------
        """Create a new table using google sheet"""
        # ------------------------------------
        login = LoginPage(page)
        login.login()

        flextable_dashboard = FlextableDashboard(page)
        flextable_dashboard.goto()
        flextable_dashboard.create_new_table()
        flextable_dashboard.verify_dashboard_table()