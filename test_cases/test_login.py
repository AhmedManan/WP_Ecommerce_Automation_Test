import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_dashboard import AdminDashboard

class TestLogin:
    load_dotenv()

    def test_verify_wordpress_login_functionality(self, page: Page):
        # ------------------------------------
        """Verify WordPress Login Functionality"""
        # ------------------------------------
        url = os.getenv("BASE_URL")
        username = os.getenv("ADMIN_USERNAME")
        password = os.getenv("ADMIN_PASSWORD")

        login = LoginPage(page)
        login.open_login(url)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        # Simple validation: admin bar appears
        admin_dashboard = AdminDashboard(page)
        admin_dashboard.is_dashboard_visible()
