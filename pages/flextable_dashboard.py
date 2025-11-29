from playwright.sync_api import Page, expect
from conftest import base_url

class FlextableDashboard:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/wp-admin/admin.php?page=gswpts-dashboard'

        # Dashboard Locators
        self.button_locator = page.get_by_role("button", name="Create new table")
        self.dashboard_heading = page.get_by_role("heading", name="All Tables")

        self.dashboard_sub_heading = page.locator("text=Manage, create and track all")
        self.dashboard_help_link = page.get_by_role("link", name="Help")
        self.dashboard_upgrade_link = page.get_by_role("link", name="Upgrade", exact=True)

        # Table Locators
        self.create_new_table_button = page.get_by_role("button", name="Create new table")
        self.url_sheet_text_field = page.get_by_role("textbox", name="Paste your Google Sheet URL")
        self.create_table_from_url_button = page.get_by_role("button", name="Create table from URL")
        self.enter_table_title_text_field = page.locator("#table-name")
        self.enter_table_description_text_field = page.get_by_role("textbox", name="Enter your table description")
        self.save_changes_button = page.get_by_role("button", name="Save changes")
        self.save_table_success_alert = page.get_by_role("alert")

        # User's Variables
        self.google_sheet_link = 'https://docs.google.com/spreadsheets/d/11qRH9xUuglOTIZa7JnWTVBYuGMT32ZhFuJ5_xypApGM/'
        self.my_table_name = 'WPPOOL Assignment Table'
        self.my_table_description = 'This table is given for performing assignment for WPPOOL QA Engineer Position'

        # Dashboard Table Verification Locators
        self.dashboard_table_locator = page.get_by_role("link", name=self.my_table_name)

    def goto(self):
        # Navigates To Dashboard
        self.page.goto(base_url+self.page_url)

    def page_fully_loaded(self):
        # Switched to 'networkidle' for better stability on dynamic content, for fully load page
        self.page.goto(base_url+self.page_url, wait_until="networkidle")

    def is_dashboard_visible(self):
        # Checks are chained for clear verification
        expect(self.dashboard_heading).to_be_visible()
        expect(self.dashboard_sub_heading).to_be_visible()
        expect(self.dashboard_help_link).to_be_visible()
        expect(self.dashboard_upgrade_link).to_be_visible()

    def create_new_table(self):
        self.create_new_table_button.click()
        self.url_sheet_text_field.fill(self.google_sheet_link)
        self.create_table_from_url_button.click()
        self.enter_table_title_text_field.fill(self.my_table_name)
        self.enter_table_description_text_field.fill(self.my_table_description)
        self.save_changes_button.click()

    def verify_dashboard_table(self):
        self.goto()
        expect(self.dashboard_table_locator).to_be_visible()
