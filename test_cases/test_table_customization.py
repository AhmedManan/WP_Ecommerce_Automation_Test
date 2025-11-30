from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard
from pages.shortcode_functionality_test_page import ShortcodeFunctionalityTestPage

class TestTableCustomization:

    def test_table_customization(self, page: Page):

        # First Perform Login
        login = LoginPage(page)
        login.login()

        flextable_dashboard = FlextableDashboard(page)
        flextable_dashboard.goto()
        flextable_dashboard.navigate_to_table_customization_title_description()

        shortcode_test_page = ShortcodeFunctionalityTestPage(page)
        shortcode_test_page.goto()
        expect(shortcode_test_page.table_title).to_be_visible()
        expect(shortcode_test_page.table_description).to_be_visible()
