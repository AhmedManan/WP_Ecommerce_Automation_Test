from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.plugin_page import PluginPage

class TestPluginPage:

    def test_flextable_plugin_activation_status(self, page: Page):
        # ------------------------------------
        """Verify FlexTable Plugin Activation Status"""
        # ------------------------------------

        # First Perform Login
        login = LoginPage(page)
        login.login()

        # Navigate to plugin page
        plugin_page = PluginPage(page)
        plugin_page.goto()

        # Check Status and Toggle Logic
        if plugin_page.activate_plugin_link.is_visible():
            print("Plugin is Deactivated. Activating...")
            # If plugin is deactivated, activate plugin
            plugin_page.activate_plugin()

        # elif plugin_page.deactivate_plugin_link.is_visible():
        #     print("Plugin is Activated. Deactivating...")
        #     # If plugin is activated, deactivate plugin
        #     plugin_page.deactivate_plugin()

        # If neither link is visible, install the plugin zip file.
        else:
            print("Plugin status links not found. Attempting to upload...")
            plugin_page.upload_plugin()

