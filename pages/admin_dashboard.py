from playwright.sync_api import Page, expect

class AdminDashboard:

    def __init__(self, page:Page):
        self.page = page

    def goto(self):
        # Admin Dashboard URL
        self.page.goto("/wp-admin")

    def is_dashboard_visible(self):
        # Check Dashboard Widgets Wrap Visibility
        return self.page.locator("#dashboard-widgets-wrap").is_visible()

    def navigate_to_plugins(self):
        # Navigate To Plugin Page
        self.page.click("#menu-plugins a")
        self.page.wait_for_url("**/wp-admin/plugins.php")