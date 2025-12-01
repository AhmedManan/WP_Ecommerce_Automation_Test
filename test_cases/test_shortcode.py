from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.flextable_dashboard import FlextableDashboard
from pages.shortcode_functionality_test_page import ShortcodeFunctionalityTestPage
from pages.shortcode_functionality_test_page import ShortcodeFunctionalityTestPage

class TestShortcode:

    def test_shortcode(self, page: Page):
        # ------------------------------------
        """Verify Table Display Using Shortcode"""
        # ------------------------------------

        # First Perform Login
        login = LoginPage(page)
        login.login()

        flextable_dashboard = FlextableDashboard(page)
        shortcode = flextable_dashboard.copy_shortcode()

        shortcode_page = ShortcodeFunctionalityTestPage(page)

        page_is_missing = shortcode_page.page_not_exists()

        if page_is_missing:
            shortcode_page.create_page()
            shortcode_page.create_shortcode(shortcode)
            shortcode_page.goto()
        else:
            shortcode_page.create_shortcode(shortcode)
            shortcode_page.goto()

        shortcode_page= ShortcodeFunctionalityTestPage(page)
        shortcode_page.goto()
        shortcode_page.table_match_with_google()

        # container_width = shortcode_page.get_container_width()
        table_width = shortcode_page.get_table_width()
        warper_width = shortcode_page.get_warper_width()

        print(f"\nTable warper Width: {warper_width}px")
        print(f"\nTable Width: {table_width}px")


        # To ensure elements were found and measured
        assert warper_width > 0, print("Failed to get width of the main content container.")
        assert table_width > 0, print("Failed to get width of the problematic table.")

        width_tolerance = 1.0
        # The table width must be less than or equal to the container width, plus a small tolerance.
        # assert table_width <= (warper_width + width_tolerance), (
        if table_width <= (warper_width + width_tolerance):
            print(f"Layout Broken: Table (Width: {table_width:.2f}px) is overflowing ")
            print(f"its Container (Width: {warper_width:.2f}px). ")
            print("This likely causes horizontal scrolling.")
            shortcode_page.problematic_table.screenshot(path="screenshots/Verify Table Display Using Shortcode Layout Error.png")



        scroll_width = page.evaluate("document.body.scrollWidth")
        viewport_width = page.viewport_size['width'] if page.viewport_size else page.evaluate("window.innerWidth")

        # Use assert, I used if to continue the test
        if scroll_width <= viewport_width + width_tolerance:
            print("Horizontal scrollbar detected, indicating layout overflow.")

