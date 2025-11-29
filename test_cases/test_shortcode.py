from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard
from pages.shortcode_functionality_test_page import ShortcodeFunctionalityTestPage

class TestShortcode:

    def test_shortcode(self, page: Page):
        # ------------------------------------
        """Verify Table Display Using Shortcode"""
        # ------------------------------------

        # First Perform Login
        login = LoginPage(page)
        login.login()

        shortcode_page = ShortcodeFunctionalityTestPage(page)

        # CALL the method and save the boolean result
        page_is_missing = shortcode_page.page_not_exists()

        # Use the SAVED variable in the conditional statement
        if page_is_missing:
            # If page is missing (page_is_missing == True), create the page first.
            shortcode_page.create_page()
            shortcode_page.create_shortcode()
        else:
            # If page exists (page_is_missing == False), skip creation and just create/update shortcode.
            shortcode_page.create_shortcode()

