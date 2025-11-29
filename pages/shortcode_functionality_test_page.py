from playwright.sync_api import Page, expect
from conftest import base_url

class ShortcodeFunctionalityTestPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/shortcode-functionality-test-page'

        # Locators for creating the page
        self.add_page_url = '/wp-admin/post-new.php?post_type=page'
        self.new_page_title = 'shortcode functionality test page'
        self.new_page_add_title = page.get_by_role("textbox", name="Add title")
        self.new_page_publish_button = page.get_by_role("button", name="Publish", exact=True)
        self.new_page_editor_publish_button = page.get_by_label("Editor publish").get_by_role("button", name="Publish", exact=True)


        # Locators if Page not exists
        self.page_not_exists_title = 'Page not found'
        self.page_not_exists_message = page.get_by_text("Opps! The page you are looking for is missing")

        # Locator if Page exists



    def goto(self):
        self.page.goto(base_url+self.page_url)

    def page_not_exists(self):
        self.goto()
        page_not_exists = self.page_not_exists_message.is_visible(timeout=500)
        print("The Value Is::::::::", page_not_exists)
        return page_not_exists

    def create_page(self):
            self.page.goto(base_url+self.add_page_url)
            self.new_page_add_title.clear()
            self.new_page_add_title.fill(self.new_page_title)
            self.new_page_publish_button.click()
            self.new_page_editor_publish_button.click()

    def create_shortcode(self):
        self.goto()
        self.page.get_by_role("menuitem", name=" Edit Page").click()

